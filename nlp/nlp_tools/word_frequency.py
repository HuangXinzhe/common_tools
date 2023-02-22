import jieba
from file.read_file import *


def frequency(file, number):
    """pycharm
    统计输入文本的词频

    :param file: 输入文本
    :param number: 需要输出的词频最高的number个
    :return: 包含词频最高的number个单词的列表
    """
    txt = open(file, "r", encoding='utf-8').read()  # read方法一次读取所有文本
    words = jieba.lcut(txt)  # lcut方法分词并返回词的列表
    counts = {}
    for word in words:
        if len(word) == 1:  # 排除单个字符的分词结果
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    word_list = []
    for i in range(number):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
        word_list.append(word)

    return word_list


def stop_words(word_list):
    """
    去除停用词

    :param word_list: 输入单词列表
    :return: 输出去除停用词的单词列表
    """

    stop_words_list = open_read_file('./data/cn_stopwords.txt')

    for word in word_list:
        if word in stop_words_list:
            word_list.remove(word)
        else:
            continue

    return word_list


if __name__ == "__main__":
    # 输入高词频单词
    # print(frequency("resume_paper.txt", 10))

    # 去除停用词
    word_list = frequency("resume_paper.txt", 10)
    print(stop_words(word_list))
