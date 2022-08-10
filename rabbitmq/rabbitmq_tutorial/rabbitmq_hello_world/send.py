#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 与RabbitMQ服务器建立连接
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True, passive=True)  # 创建一个hello队列，消息将传递到该队列

channel.basic_publish(exchange='',  # 消息永远不能直接发送到队列，它总是需要通过交换，使用空字符串标识为默认交换，这种交换是特殊的，允许准确地指定消息应该去哪个队列
                      routing_key='hello',  # 指定队列名称
                      body='Hello World!')  # 传输的内容

print(" [x] Sent 'Hello World!'")

connection.close()  # 确保网络缓冲区已被刷新，并且消息实际上已传递到RabbitMQ，通过关闭连接完成



