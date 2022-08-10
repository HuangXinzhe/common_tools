# coding=utf-8
### 生产者
import pika
import time
user_info = pika.PlainCredentials('guest', 'guest')#用户名和密码
# connection = pika.BlockingConnection(pika.ConnectionParameters('ip', 5672, '/', user_info))#连接服务器上的RabbitMQ服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', user_info))#连接服务器上的RabbitMQ服务
# 创建一个channel
channel = connection.channel()
# 如果指定的queue不存在，则会创建一个queue，如果已经存在 则不会做其他动作，官方推荐，每次使用时都可以加上这句
channel.queue_declare(queue='hello')
for i in range(0, 10):
    channel.basic_publish(exchange='',#当前是一个简单模式，所以这里设置为空字符串就可以了
                          routing_key='hello',# 指定消息要发送到哪个queue
                          body='{}'.format(i)# 指定要发送的消息
                          )
    time.sleep(1)
# 关闭连接
connection.close()