import platform
import sys
import os
def showENV():  # 函数
    s = platform.platform()
    print("当前系统：", s)  # 获取系统信息
    p = sys.path
    print("当前安装路径：", p)  # 获取安装路径
    op = os.getcwd()
    print("当前代码路径：", op)  # 获取当前代码路径
    print("Python版本信息：", sys.version_info)

if __name__ == '__main__':
    showENV()