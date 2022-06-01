import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Accuracy, Precision, Recall
import tensorflow_addons as tfa
from tqdm import tqdm
import sys


class BiGRUCRF(tf.keras.Model):
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
        # self.Hidden = layers.GRU(64, return_sequences=True)
        self.Hidden = layers.Bidirectional(layers.GRU(64, return_sequences=True))
        self.Output = tfa.layers.CRF(self.tag_size)


    def call(self, inputs):
        X, mask = inputs
        mask = tf.where(mask == 1, True, False)
        hidden = self.Hidden(X, mask=mask)
        return self.Output(hidden, mask)
