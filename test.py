from nlp.vector.setence2vector import *

# 读取模型
vector = joblib.load('nlp/crf_model/model/sentence_to_vector.pkl')


print(vector.get_vector(['好开心啊又可以吃成长快乐']))