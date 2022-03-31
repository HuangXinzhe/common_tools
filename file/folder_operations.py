"""
获取当前文件夹路径、当前文件夹下子文件夹和当前文件夹下文件
"""

import os


def file_name(file_dir):
    """get root,dirs and files

    1.Gets the current directory path
    2.Gets all subdirectories under the current path
    3.Gets all non-directory subfiles under the current path

    Args:
        file_dir:The current path

    Returns:
        You can change the code to choose the return you want.
        1.root:current directory path and return a string
        2.dirs:all subdirectories under the current path and return a list
        3.files:all non-directory subfiles under the current path adn return a list
    """

    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

        return files


if __name__ == "__main__":
    print(file_name(r'C:\Users\86183\Desktop\简历项目资料'))


