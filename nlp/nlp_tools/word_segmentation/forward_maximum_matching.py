def load_dict(txt):
    f = open(txt)  # 词典文件，每行存储一个单词
    lexicon = set()
    max_len = 0
    for line in f:
        word = line.strip()
        lexicon.add(word)
        if len(word) > max_len:
            max_len = len(word)
    f.close()

    return lexicon, max_len


def fmm_word_seg(sentence, lexicon, max_len):
    """
    sentence：待分词的句子
    lexicon：词典（所有单词集合）
    max_len：词典中最长单词长度
    """
    begin = 0
    end = min(begin + max_len, len(sentence))
    words = []
    while begin < end:
        word = sentence[begin:end]
        if word in lexicon or end - begin == 1:  # 判断被切分的单词是否在词典中，当被切分的词不存在在词典中，但是仅有一个字符时也可
            words.append(word)
            begin = end
            end = min(begin + max_len, len(sentence))
        else:  # 此时被切分的单词未在词典中，则将被切词长度减少一个
            end -= 1
    return words


if __name__ == "__main__":
    lexicon, max_len = load_dict("lexicon.txt")  # lexicon为词典集合，max_len为词典中最长单词的长度
    words = fmm_word_seg(input("请输入句子："), lexicon, max_len)

    for word in words:
        print(word, )
