# coding:utf-8
import jieba
import gensim
from gensim.models.doc2vec import Doc2Vec
import re
from file.read_file import *

TaggededDocument = gensim.models.doc2vec.TaggedDocument


def get_datasest():

    list_data = open_read_file('D:/resume/resume-ai/resume_project/model/data/IT_label/feature_label_data.txt')

    list_txt_all = []
    for data in list_data:
        list_txt_all += eval(data)[0]

    stop_list = [line[:-1] for line in open('../../data/cn_stopwords.txt', 'r', encoding='utf-8')]
    result = []
    for each in list_txt_all:
        each_cut = jieba.cut(each)
        each_split = ' '.join(each_cut).split()
        each_result = [word for word in each_split if word not in stop_list]
        result.append(' '.join(each_result))

    train_data = []
    for line_number, text in enumerate(result):
        word_list = text.split(' ')
        l = len(word_list)
        word_list[l - 1] = word_list[l - 1].strip()
        TaggededDocument = gensim.models.doc2vec.TaggedDocument
        document = TaggededDocument(word_list, tags=[line_number])
        train_data.append(document)

    return train_data


def train(x_train, size=100, epoch_num=1):  ##size 是你最终训练出的句子向量的维度，自己尝试着修改一下

    model_dm = Doc2Vec(x_train, min_count=1, window=5, vector_size=size, sample=1e-3, negative=5, workers=4)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=70)
    model_dm.save('model/model_doc_2_vec/vec_100.pkl')  ##模型保存的位置

    return model_dm


def ceshi(str1):
    model_dm = Doc2Vec.load('model/model_doc_2_vec/vec_100.pkl')
    ##此处需要读入你所需要进行提取出句子向量的文本   此处代码需要自己稍加修改一下
    # str1 = '2018年03月23日晚上大概十一点多钟我和张三骑着摩托车从住处出门想看看有什么能吃的东西.'
    ##你需要进行得到句子向量的文本，如果是分好词的，则不需要再调用结巴分词

    # test_text = ' '.join(jieba.cut(str1)).encode('utf-8').split('')
    test_text = ' '.join(jieba.cut(str1)).split(' ')

    inferred_vector_dm = model_dm.infer_vector(test_text)  ##得到文本的向量
    # print(inferred_vector_dm)

    return inferred_vector_dm


if __name__ == '__main__':
    # x_train = get_datasest()
    # model_dm = train(x_train)

    # doc_2_vec = ceshi()
    # print(type(doc_2_vec))
    # print(doc_2_vec.shape)

    # print(get_datasest())

    list_data = open_read_file('D:/resume/resume-ai/resume_project/model/data/IT_label/feature_label_data.txt')
    # print(eval(list_data[0])[0])
    # all_vector = []
    for data in list_data:
        sentence_vector = []
        # print(eval(data)[2])
        for sentence in eval(data)[0]:
            sentence_vector.append(ceshi(sentence))

        sample = [sentence_vector, eval(data)[2]]

        with open('sentence_data.txt', 'a+', encoding='utf-8') as f:
            f.write(str(sample))
            f.write('\n')




        # sentence_vector_1 = []
        # for i in sentence_vector:
        #     sentence_vector_1.append(i)
        # all_vector.append(sentence_vector)
        # print(all_vector)






