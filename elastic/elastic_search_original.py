from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'author': 'author_name',
    'text': 'Interesting content...',
    'timestamp': datetime.now(),
}

# 写入数据
res = es.index(index="test-index", id=1, document=doc)
print(res['result'])


# 读取数据
res = es.get(index="test-index", id=1)
print(res['_source'])