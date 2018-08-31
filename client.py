# -*- coding:utf-8 -*-

import paho.mqtt.client as mqtt
import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf8')

host = '127.0.0.1'
port = '1883'
topic = 'test'

def on_msg_come(client,userdata,msg):
    print msg.topic + ":" + msg.payload

def on_connect(client, userdata, flags, rc):
    print 'Connected with result code :' + str(rc)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print 'Unexpected disconnection :'  + str(rc)

def test():
    msg = str(datetime.datetime.now())
    client = mqtt.Client()
    client.on_connect = on_connect  # 设置连接上服务器回调函数
    client.on_message = on_msg_come  # 设置接收到消息回调函数
    client.on_disconnect = on_disconnect  # 设置client失去连接回调函数
    client.connect(host, port, 60)
    client.subscribe(topic, qos=0)
    client.publish(topic, payload=msg, qos=0)
    client.loop_forever()

if __name__ == "__main__":
    test()



