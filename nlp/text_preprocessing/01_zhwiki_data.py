# 安装专门用于处理维基百科的快照
# pip install wikiextractor

# 维基百科快照文件
# $ python -m wikiextractor.WikiExtractor

# WikiExtractor工具包使用的参数
# $ python -m wikiextractor.WikiExtractor -h

"""
处理玩获得的纯文本语料文件
text文件由AA到AO子文件夹组成，每个子文件夹包含wiki_00至wiki_99
每个数据以<doc>开始并以</doc>结束
./text
  |- AA
    |- wiki_00
    |- wiki_01
    |- ...
    |- wiki_99
  |- AB
  |- ...
  |- AO
"""