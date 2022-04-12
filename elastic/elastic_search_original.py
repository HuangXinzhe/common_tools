from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

##########################################################################################
# doc = {
#     'author': 'author_name',
#     'text': 'Interesting content...',
#     'timestamp': datetime.now(),
# }

# 写入数据
# res = es.index(index="test-index", id=1, document=doc)
# print(res['result'])

##########################################################################################
# 读取数据
# res = es.get(index="test-index", id=1)
# print(res['_source'])

##########################################################################################
# 刷新索引
# es.indices.refresh(index="test-index")

##########################################################################################
# 搜索文档
"""
{
    "took": 1,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 3,
            "relation": "eq"
        },
        "max_score": 1,
        "hits": [
            {
                "_index": "test-index",
                "_type": "_doc",
                "_id": "1",
                "_score": 1,
                "_source": {
                    "author": "黄昕哲",
                    "text": "训练",
                    "timestamp": "2022-04-08T09:17:02.912087"
                }
            }
            ,
            {
                "_index": "test-index",
                "_type": "_doc",
                "_id": "2",
                "_score": 1,
                "_source": {
                    "author": "郝海江",
                    "text": "验证",
                    "timestamp": "2022-04-08T09:17:30.081602"
                }
            }
            ,
            {
                "_index": "test-index",
                "_type": "_doc",
                "_id": "3",
                "_score": 1,
                "_source": {
                    "author": "王洋",
                    "text": "测试",
                    "timestamp": "2022-04-08T09:17:54.518285"
                }
            }
        ]
    }
}
"""
# resp = es.search(index="test-index", query={"match_all": {}})
# print("Got %d Hits:" % resp['hits']['total']['value'])
# for hit in resp['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

##########################################################################################
# 更新文档
# from datetime import datetime
# from elasticsearch import Elasticsearch
#
# es = Elasticsearch()

# doc = {
#     'author': "徐国栋",
#     'text': "亮亮你怎么看",
#     'timestamp': datetime.now(),
# }
# res = es.update(index="test-index", id=5, body=doc)
# print(res['result'])

##########################################################################################
# 删除文档
# es.delete(index="test-index", id=4)

##########################################################################################

