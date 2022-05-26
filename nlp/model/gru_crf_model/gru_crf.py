import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Accuracy, Precision, Recall
import tensorflow_addons as tfa
from tqdm import tqdm
import sys


class GRU_CRF(tf.keras.Model):
    def __init__(self, tag_size):
        super().__init__()
        # 超参定义
        self.tag_size = tag_size
        self.checkpoint_dir = None
        self.best_accuracy = None
        self.patience = 0
        # 模型结构定义
        self.Embed = None
        # self.Hidden = [layers.GRU() for i in range(3)]
        self.Hidden = layers.GRU(64, return_sequences=True)
        self.Output = tfa.layers.CRF(self.tag_size)
        #
        self.optimizer = Adam(learning_rate=0.001)
        self.loss_fun = self.CRF_loss
        # metrics
        self.accuracy = Accuracy()
        self.precision = Precision()
        self.recall = Recall()

    def call(self, inputs):
        X, mask = inputs
        mask = tf.where(mask == 1, True, False)
        hidden = self.Hidden(X, mask=mask)
        return self.Output(hidden, mask)

    def train(self, train_data, valid_data=None
              , epochs=10, gard_theta=1
              , patience = None, min_delta = 1e-3
              , checkpoint_dir='./checkpoints/'
              , init_best_accuracy=0
              , verbose=0):
        #
        self.best_accuracy = init_best_accuracy
        loss_pre_epoch = {
            'tra_loss': [], 'val_loss': []
        }
        metrics_pre_epoch = {
            'val_accuracy': []
            , 'val_precision': []
            , 'val_recall': []
            , 'val_F1score': []
        }
        for epoch in range(epochs):
            # 初始化
            loss_pre_batch = []
            #
            for step, b_data in enumerate(tqdm(train_data, desc='step')):
                X, y, mask = b_data
                with tf.GradientTape(persistent=True) as tape:
                    y_pred, emission, real_len, transition = self([X, mask])
                    loss = self.loss_fun(emission, y, real_len, transition)
                # 参数更新
                train_varb = self.trainable_variables
                grads = tape.gradient(loss, train_varb)
                grads = self.grad_clipping(grads, gard_theta)  # 梯度裁剪
                self.optimizer.apply_gradients(zip(grads, train_varb))
            # record
                loss_pre_batch.append(loss.numpy())
                if verbose != 0 and step % verbose == 0:
                    print(
                        'step ', step, ' '
                        , 'tra_loss:', np.mean(loss_pre_batch)
                    )
            loss_pre_epoch['tra_loss'].append(np.mean(loss_pre_batch))
            if valid_data is not None:
                X, y, mask = valid_data
                y_pred, emission, real_len, transition = self([X, mask])
                loss = self.loss_fun(emission, y, real_len, transition)
                #
                self.accuracy.update_state(y, y_pred, mask)
                accuracy = self.accuracy.result().numpy()
                precision = self.MulClassMetric(self.precision, y, y_pred, mask)
                recall = self.MulClassMetric(self.recall, y, y_pred, mask)
                F1score = self.F1_score(precision, recall)
                # record
                loss_pre_epoch['val_loss'].append(loss.numpy())
                metrics_pre_epoch['val_accuracy'].append(accuracy)
                metrics_pre_epoch['val_precision'].append(precision)
                metrics_pre_epoch['val_recall'].append(recall)
                metrics_pre_epoch['val_F1score'].append(F1score)
                print(
                    'epoch ', epoch, ' '
                    , 'tra_loss:', loss_pre_epoch['tra_loss'][-1], ' '
                    , 'val_loss:', loss_pre_epoch['val_loss'][-1], ' '
                    , 'val_accuracy:', metrics_pre_epoch['val_accuracy'][-1], ' '
                    , 'val_precision:', metrics_pre_epoch['val_precision'][-1], ' '
                    , 'val_recall:', metrics_pre_epoch['val_recall'][-1], ' '
                    , 'val_F1score:', metrics_pre_epoch['val_F1score'][-1]
                    , '\n'
                )
                # best model save
                if accuracy > self.best_accuracy:
                    self.save_weights(checkpoint_dir + 'best_model')
                    self.best_accuracy = accuracy
            else:
                print(
                    'epoch ', epoch, ' '
                    , 'tra_loss:', loss_pre_epoch['tra_loss'][-1], ' '
                    , '\n'
                )
            # min Early Stopping
            if patience is not None and len(metrics_pre_epoch['val_accuracy']) > 1:
                # diff = metrics_pre_epoch['val_accuracy'][-2] - metrics_pre_epoch['val_accuracy'][-1] \
                #     if early_stop_mode == 'min' else metrics_pre_epoch['val_accuracy'][-1] - metrics_pre_epoch['val_accuracy'][-2]
                if metrics_pre_epoch['val_accuracy'][-2] - metrics_pre_epoch['val_accuracy'][-1] <= min_delta:
                    self.patience += 1
                else:
                    self.patience = 0
                if self.patience > patience:
                    break


        return loss_pre_epoch, metrics_pre_epoch

    def grad_clipping(self, grads, theta):
        """
        梯度裁剪
        """
        theta = tf.constant(theta, dtype=tf.float32)
        new_grads = [tf.convert_to_tensor(grad) if isinstance(grad, tf.IndexedSlices) else grad for grad in grads]
        norm = tf.math.sqrt(sum(tf.reduce_sum(grad ** 2).numpy() for grad in new_grads))
        norm = tf.cast(norm, tf.float32)
        if tf.greater(norm, theta):
            new_grads = [(grad * theta) / norm for grad in new_grads]
        return new_grads

    def CRF_loss(self, emission, y_true, real_len, transition):
        loss, _ = tfa.text.crf_log_likelihood(
            emission, y_true, real_len, transition
        )
        return tf.reduce_mean(-loss)

    def F1_score(self, precision, recall):
        return 2 * precision * recall / (precision + recall)

    def MulClassMetric(self, metric, y_true, y_pred, mask):
        temp = []
        for i in range(self.tag_size):
            metric.reset_states()
            metric.update_state(
                tf.where(y_true == i, 1, 0), tf.where(y_pred == i, 1, 0), mask
            )
            temp.append(
                metric.result().numpy()
            )
        return np.mean(temp)
