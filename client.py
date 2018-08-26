# -*- coding:utf-8 -*-

import paho.mqtt.client as mqtt
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

host = '127.0.0.1'
port = '1883'
topic = 'test'
payload = 'hello'
qos = 0

# # 连接mqtt服务器
# def on_mqtt_connect():
#     client.connect(host,port,60)

def on_msg_come(client,userdata,msg):
    print msg.topic + ":" + msg.payload

def on_connect(client, userdata, flags, rc):
    print 'Connected with result code :' + str(rc)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print 'Unexpected disconnection :'  + str(rc)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect  # 设置连接上服务器回调函数
    client.on_message = on_msg_come  # 设置接收到消息回调函数
    client.on_disconnect = on_disconnect  # 设置client失去连接回调函数
    client.connect(host, port, 60)  # 连接mqtt服务器
    client.subscribe(topic, qos)  # 订阅主题

    for i in range(1, 10):
        print i
        client.publish(topic, i, 0)  # 发布主题
        time.sleep(0.1)

    client.loop_forever()  # client调用disconnect()才会返回。自动处理重连接

if __name__ == "__main__":
    main()



