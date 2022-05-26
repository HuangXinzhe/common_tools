from itertools import chain
import nltk
import sklearn
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics

from data_processing import *
from collections import Counter

import matplotlib.pyplot as plt

plt.style.use('ggplot')

# 1、数据集划分
data, label = feature_data('../../data/crf_data.txt')

X_train = data[:10]
y_train = label[:10]

X_test = data[341:]
y_test = label[341:]

# 2、训练模型
crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    max_iterations=100,
    all_possible_transitions=True
)

params_space = {
    'c1': scipy.stats.expon(scale=0.5),
    'c2': scipy.stats.expon(scale=0.05),
}

# labels = list(crf_model.classes_)  # 生成标签列表，只有在crf模型训练完成才能使用
# labels.remove('O')  # 如果有O可以先删除所有的O
labels = ['B-basic',
          'I-basic',
          'B-work',
          'I-work',
          'B-project',
          'I-project',
          'B-education',
          'I-education',
          'B-advantage',
          'I-advantage',
          'B-skill',
          'I-skill',
          'B-others',
          'I-others',
          'B-certificate',
          'I-certificate',
          'B-activity',
          'I-activity',
          'B-language',
          'I-language']

# use the same metric for evaluation
f1_scorer = make_scorer(metrics.flat_f1_score,
                        average='weighted', labels=labels)

# search
rs = RandomizedSearchCV(crf, params_space,
                        cv=3,
                        verbose=1,
                        n_jobs=-1,
                        n_iter=50,
                        scoring=f1_scorer)
rs.fit(X_train, y_train)

# crf_model = rs.best_estimator_
print('best params:', rs.best_params_)
print('best CV score:', rs.best_score_)
print('model size: {:0.2f}M'.format(rs.best_estimator_.size_ / 1000000))
print('==========================================================================================')

# 参数空间
means = rs.cv_results_['mean_test_score']
params = rs.cv_results_['params']
for mean, param in zip(means, params):
    print("%f  with:   %r" % (mean, param))
print('==========================================================================================')

# 检查参数空间
_x = [s['c1'] for s in rs.cv_results_['params']]
_y = [s['c2'] for s in rs.cv_results_['params']]
_c = [s for s in rs.cv_results_['mean_test_score']]

fig = plt.figure()
fig.set_size_inches(12, 12)
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('C1')
ax.set_ylabel('C2')
ax.set_title("Randomized Hyperparameter Search CV Results (min={:0.3}, max={:0.3})".format(
    min(_c), max(_c)
))

ax.scatter(_x, _y, c=_c, s=60, alpha=0.9, edgecolors=[0, 0, 0])

print("Dark blue => {:0.4}, dark red => {:0.4}".format(min(_c), max(_c)))
plt.show()
print('==========================================================================================')

crf = rs.best_estimator_
y_pred = crf.predict(X_test)
sorted_labels = sorted(labels, key=lambda name: (name[1:], name[0]))

print(metrics.flat_classification_report(
    y_test, y_pred, labels=sorted_labels, digits=3
))


def print_transitions(trans_features):
    for (label_from, label_to), weight in trans_features:
        print("%-6s -> %-7s %0.6f" % (label_from, label_to, weight))


print("Top likely transitions:")
print_transitions(Counter(crf.transition_features_).most_common(20))

print("\nTop unlikely transitions:")
print_transitions(Counter(crf.transition_features_).most_common()[-20:])
