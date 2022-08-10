import os


def file_name(file_dir):
    """读取所有Excel数据文件名

    :param file_dir: 数据文件所在当前文件夹名
    :return: 返回当前夹下所有数据文件名的列表
    """

    for root, dirs, files in os.walk(file_dir):
        return files
