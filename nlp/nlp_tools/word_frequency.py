import jieba


def frequency(file, number):
    """
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


if __name__ == "__main__":
    print(frequency("resume_paper.txt", 10))
