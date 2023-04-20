import nltk

"""
下载语料库与词典资源
若因为网络等原因可以在GitHub上自行下载
https://github.com/nltk/nltk_data/tree/gh-pages
将其中package更名为nltk_data，并放置在根目录中
"""
# nltk.download()


# ====================================停用词====================================
from nltk.corpus import stopwords
# print(stopwords.words('english'))  # 查看英文停用词



# ====================================常用数据集====================================
from nltk.corpus import gutenberg
# print(gutenberg.raw("austen-emma.txt"))  # 古腾堡语料库

from nltk.corpus import sentence_polarity
# print(sentence_polarity.categories())  # 标签类别
# print(sentence_polarity.words())  # 语料库中单词列表
# print(sentence_polarity.words(categories="pos"))  # 语料库中对应类别单词列表"pos"，"neg"
# print(sentence_polarity.sents())  # 语料库中句子列表



# ====================================常用词典====================================
from nltk.corpus import wordnet
# syns = wordnet.synsets("bank")  # 返回"bank"所有词义
# print(syns[0].name())  # 返回第一个词义名称
# print(syns[0].difinition())  # 返回第一个词义定义
# print(syns[0].example())  # 返回第一个词义的使用示例
# print(syns[0].hypernyms())  # 返回第一个词义的上位同义词集合
# dog = wordnet.synset('dog.n.01')
# cat = wordnet.synset('cat.n.01')
# print(dog.wup_similarity(cat))  # 计算两个同义词集合之间的Wu-Palmer相似度



from nltk.corpus import sentiwordnet

# 有情感标注的词典
# print(sentiwordnet.senti_synset('good.a.01'))  # <good.a.01: PosScore=0.75 NegScore=0.0>



# ====================================常用自然语言处理工具====================================
# 分句
from nltk.tokenize import sent_tokenize
# text = gutenberg.raw("austen-emma.txt")
# sentences = sent_tokenize(text)
# print(sentences[100])  # 显示一个句子

# 标记解析
from nltk.tokenize import word_tokenize
# print(word_tokenize(sentences[100]))

# 词性标注
from nltk import pos_tag
# print(pos_tag(word_tokenize("They sat by the fire.")))
# print(nltk.help.upenn_tagset())  # 返回全部词性标记集以及各词性的示例
# print(nltk.help.upenn_tagset('NN'))

# 其他工具
# 命名实体识别、组块分析、句法分析