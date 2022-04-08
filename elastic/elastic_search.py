from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()


def write_data(index_name, id_number, document_context):
    """
    将数据写入ElasticSearch

    :param index_name:索引名
    :param id_number:id
    :param document_context:将要写入的数据
    :return:返回输入数据的反馈
    """

    res = es.index(index=index_name, id=id_number, document=document_context)

    return res


def get_data(index_name, id_number):
    """
    读取数据

    :param index_name: 索引名
    :param id_number: id
    :return: 返回对应索引和id的数据
    """

    res = es.get(index=index_name, id=id_number)

    return res

def refresh_data(index_name):
    """


    :param index_name:
    :return:
    """

    es.indices.refresh(index=index_name)


if __name__ == "__main__":
    # 1. 数据输入测试
    # doc = {
    #     'author': '王洋',
    #     'text': '测试',
    #     'timestamp': datetime.now(),
    # }
    #
    # res = write_data("test-index", 3, doc)
    # print(res['result'])

    # 2. 读取数据
    res = get_data("test-index", 1)
    print(res['_source'])
