import re


def open_read_file(file):
    """
    打开读取文本数据每行，并保存在列表中

    :param file:要打开读取的文件名
    :return:返回
    """

    with open(file, 'r', encoding='utf-8') as f:
        file_list = f.readlines()
        file_list = [re.sub('\n', '', i) for i in file_list]

    return file_list
