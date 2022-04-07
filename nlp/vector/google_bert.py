"""
使用前需要启动服务：bert-serving-start -model_dir D:\PycharmProjects\chinese_L-12_H-768_A-12
"""

from bert_serving.client import BertClient
import numpy as np


def main():
    bc = BertClient()
    doc_vecs = bc.encode(['今天天空很蓝，阳光明媚', '今天天气好晴朗', '现在天气如何', '自然语言处理', '机器学习任务'])

    print(doc_vecs)


if __name__ == '__main__':
    main()