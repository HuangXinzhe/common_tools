import gensim
import jieba
import pandas as pd
import os
from gensim.models.doc2vec import Doc2Vec
from file.folder_operations import file_name
import re
from file.read_file import open_read_file

import joblib


class SentenceToVector(object):
    """
    以句子为单位的训练得出句子向量
    """

    def __init__(self, text, stop_words_path):
        self.text = text
        self.stop_words_path = stop_words_path

    def cut_sentence(self):
        """
        去除输入的句子文本中的停用词

        :return: 返回去除停用词的句子
        """

        stop_list = [line[:-1] for line in open(self.stop_words_path, 'r', encoding='utf-8')]
        result = []
        for each in self.text:
            each_cut = jieba.cut(each)
            each_split = ' '.join(each_cut).split()
            each_result = [word for word in each_split if word not in stop_list]
            result.append(' '.join(each_result))
        return result

    def make_data(self):
        """
        制作Doc2Vec训练所需要的输入数据形式

        :return:返回形如[句子，句子序号]的数据形式
        """

        train_data = []
        for line_number, text in enumerate(self.cut_sentence()):
            word_list = text.split(' ')
            l = len(word_list)
            word_list[l - 1] = word_list[l - 1].strip()
            TaggededDocument = gensim.models.doc2vec.TaggedDocument
            document = TaggededDocument(word_list, tags=[line_number])
            train_data.append(document)
        return train_data

    def train_model(self):
        doc2vec_model = Doc2Vec(self.make_data(), vector_size=20, min_count=1, window=3, sample=1e-3, workers=4)
        doc2vec_model.train(self.make_data(), total_examples=doc2vec_model.corpus_count, epochs=10)
        return doc2vec_model

    def get_vector(self, target_sentence):
        sentence_vector = self.train_model().infer_vector(doc_words=target_sentence, alpha=0.025)
        return sentence_vector


if __name__ == "__main__":
    # files = file_name('D:/resume/resume-ai/resume_project/feature/data/IT_txt/')
    # list_sum = []
    # for file in files:
    #     text = open_read_file('D:/resume/resume-ai/resume_project/feature/data/IT_txt/{}'.format(file))
    #     list_sum += text

    # list_sum = ['好开心啊又可以吃成长快乐']
    # 
    # s_vector = SentenceToVector(list_sum, '../data/cn_stopwords.txt')
    # 
    # print(s_vector.cut_sentence())
    # print(s_vector.make_data())
    # 
    # s_vector.train_model()

    # print(s_vector.get_vector(['好开心啊又可以吃成长快乐']))

    list_data = open_read_file('D:/resume/resume-ai/resume_project/model/data/IT_label/feature_label_data.txt')
    # print(eval(list_data[0])[0])

    list_txt_all = []
    for data in list_data:
        list_txt_all += eval(data)[0]

    # s_vector = SentenceToVector(list_txt_all, '../../data/cn_stopwords.txt')

    # s_vector.train_model()

    for data in list_data:
        sentence_vector = []
        for sentence in eval(data)[0]:
            print([sentence])

            # sentence_vector += s_vector.get_vector([sentence])
        break
        # with open('../result/sentence_vector.txt', 'a+', encoding='utf-8') as f:
        #     f.write(str(sentence_vector))
        #     f.write('\n')
