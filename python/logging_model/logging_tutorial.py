import logging

"""
日志级别分为五个级别
DEBUG：用来记录详细的信息，方便定位问题进行调试，在生产环境一般不开启
INFO：记录关键代码点的信息，一遍代码是否按照预期的执行，生产环境通常会设置INFO级别
WARNING：记录不被预期发生的情况，如磁盘不足
ERROR：由于一个更重要的问题导致某些功能不能正常运行的记录的信息
CRITICAL：当发生严重错误，导致应用程序不能继续运行时记录的信息

日志的重要级别逐次提高，默认级别是warning，低于warning的日志信息都不会输出
"""
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warn")
# logging.error("this is error")
# logging.critical("this is critical")




"""
修改日志级别
logging.basicConfig
"""
# logging.basicConfig(level=logging.DEBUG)




"""
日志记录到文件
logging.basicConfig
默认为追加写，想要改变模式需要指定filemode='w'
"""
# logging.basicConfig(filename="test.log", level=logging.INFO)
# logging.debug("this is debug")
# logging.info("this is info")
# logging.error("this is error")



"""
指定日志格式
默认输出的格式为
日志级别：日志记录器名：日志内容

astime：%(astime)s，日志合适被创建
levelname：%(levelname)s，日子级别
message：%(message)s，日志内容
name：%(name)s，日志记录器名
process：%(process)s，进程ID
thread：%(thread)s，线程ID
"""
# logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s')
# logging.error("this is error")



"""
记录器
日志记录是通过日志记录器的实例对象创建的，每个记录器都有一个名字，系统默认创建名为root，这个记录器是根记录器。
记录器支持层级结构，子记录器通常不需要单独设置日志界别以及Handler，如果子记录器没有单独设置，则它的行为会委托给父级

记录器名称可以是任意名称
最佳实践是直接用模块的名称当作记录器的名字
"""
# logging = logging.getLogger(__name__)



"""
处理器
处理记录器记录的内容位置

Python内置很多实用处理器，常用的有：
1、StreamHandler标准处理器，将消息发送到标准输出流、错误流
2、FileHandler文件处理器，将消息发送到文件
3、RotatingFileHandler文件处理器，文件达到指定大小后，弃用新文件存储日志
4、TimedRotatingFileHandler文件处理器，日志以特定的时间间隔轮换日志文件

Handler
    setLevel
    setFormatter
    addFilter()
    removeFilter()
"""
# from logging import StreamHandler
# from logging import FileHandler
#
# logger = logging.getLogger(__name__)
#
# # 设置为DEBUG级别
# logger.setLevel(logging.DEBUG)
#
# # 标准流处理器，设置的级别为WARAING
# stream_handler = StreamHandler()
# stream_handler.setLevel(logging.WARNING)
# logger.addHandler(stream_handler)
#
# # 文件处理器，设置的级别为INFO
# file_handler = FileHandler(filename="test.log")
# file_handler.setLevel(logging.INFO)
# logger.addHandler(file_handler)
#
# logger.debug("this is debug")
# logger.info("this is info")
# logger.error("this is error")
# logger.warning("this is warning")



"""
格式器
格式器可以以对象的形式设置在Handler上

注意
格式器只能作用在处理器上，通过处理器的setFromatter方法设置格式器。而且一个Handler只能设置一个格式器。是一对一的关系。
而logger与handler是一对多的关系，一个logger可以添加多个handler。handler和logger都可以设置日志的等级。
"""
# import logging
# from logging import StreamHandler
#
# logger = logging.getLogger(__name__)
#
# # 标准流处理器
# stream_handler = StreamHandler()
# stream_handler.setLevel(logging.WARNING)
#
# # 创建一个格式器
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # 作用在handler上
# stream_handler.setFormatter(formatter)
# # 添加处理器
# logger.addHandler(stream_handler)
#
# logger.info("this is info")
# logger.error("this is error")
# logger.warning("this is warning")



"""
logging.basicConfig
1、创建一个root记录器
2、设置root的日志级别为warning
3、为root记录器添加StreamHandler处理器
4、为处理器设置一个简单格式器
"""
# # 第一种写法
# logging.basicConfig()
# logging.warning("hello")
#
# # 第二种写法
# import sys
# import logging
# from logging import StreamHandler
# from logging import Formatter
#
#
# logger = logging.getLogger("root")
# logger.setLevel(logging.WARNING)
# handler = StreamHandler(sys.stderr)
# logger.addHandler(handler)
# formatter = Formatter(" %(levelname)s:%(name)s:%(message)s")
# handler.setFormatter(formatter)
# logger.warning("hello")



"""
日志配置
"""
# import logging.config
#
# # 加载配置
# logging.config.fileConfig('logging.conf')
#
# # 创建 logger
# logger = logging.getLogger()
#
# # 应用代码
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
