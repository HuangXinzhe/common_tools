import getenv  # 导入自定义模块getenv

def showENV():  # 实现同名函数showENV
    print("this is my env")

showENV()  # 调用本地函数
getenv.showENV()  # 调用getenv模块里的函数