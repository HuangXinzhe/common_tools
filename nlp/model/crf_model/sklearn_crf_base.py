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
import matplotlib_note.pyplot as plt
from data_processing import *

plt.style.use('ggplot')

# 1、数据集划分
data, label = feature_data('../../data/crf_data.txt')

X_train = data[:100]
y_train = label[:100]

X_test = data[341:]
y_test = label[341:]

# 2、训练模型
crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)
crf.fit(X_train, y_train)

labels = list(crf.classes_)  # 生成标签列表
# labels.remove('O')  # 如果有O可以先删除所有的O

# 3、评估
y_pred = crf.predict(X_test)

# f1_score
f1_score = metrics.flat_f1_score(y_test, y_pred, average='weighted', labels=labels)
print("f1_score:", f1_score)

# accuracy
accuracy = metrics.flat_accuracy_score(y_test, y_pred)
print("accuracy:", accuracy)

# recall
recall = metrics.flat_recall_score(y_test, y_pred, average='weighted', labels=labels)
print("recall:", recall)

# precision
precision = metrics.flat_precision_score(y_test, y_pred, average='weighted', labels=labels)
print("precision:", precision)


# group B and I results
sorted_labels = sorted(
    labels,
    key=lambda name: (name[1:], name[0])
)
print(metrics.flat_classification_report(
    y_test, y_pred, labels=sorted_labels, digits=3
))
