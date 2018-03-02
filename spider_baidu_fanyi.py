# -*- coding: UTF-8 -*-
import json
from urllib import parse
from urllib import request
from threading import Thread,Condition
import time

def en_zh(Form_Data,Request_URL,lock):
    lock.acquire()
    while True:
        Form_Data['from'] = 'en'
        Form_Data["to"] = 'zh'
        word = input("input(en):")
        if word==r"\zh":
            lock.notify()
            lock.wait()
            continue
        else:
            Form_Data["query"] = word
            data = get_data(Form_Data, Request_URL)
            print("output(zh):{}".format(data))

def zh_en(Form_Data,Request_URL,lock):
    lock.acquire()
    while True:
        Form_Data['from'] = 'zh'
        Form_Data["to"] = 'en'
        word = input("input(zh):")
        if word==r"\en":
            lock.notify()
            lock.wait()
            continue
        else:
            Form_Data["query"] = word
            data=get_data(Form_Data,Request_URL)
            print("output(en):{}".format(data))

def get_data(Form_Data,Request_URL):
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL, data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    translate_result = translate_results['trans_result']['data'][0]['dst']
    return translate_result

def main():
    lock=Condition()
    Request_URL = 'http://fanyi.baidu.com/v2transapi'
    Form_Data = {}
    Form_Data['from'] = 'zh'
    Form_Data["to"] = 'en'
    Form_Data["transtype"] = 'translang'
    Form_Data["simple_means_flag"] = '3'

    t1 = Thread(target=en_zh, args=(Form_Data, Request_URL, lock))
    t2 = Thread(target=zh_en, args=(Form_Data, Request_URL, lock))
    t1.start()
    time.sleep(0.5)
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
