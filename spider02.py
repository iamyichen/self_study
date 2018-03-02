# -*- coding: UTF-8 -*-
from urllib import request
import re

#在调用func()方法前后分别打印出来本地外网ip
def test_ip(func):
    def wrapper(*args,**kwargs):
        print("befoe {}() function,my ip is:".format(func.__name__),get_myip())
        res=func(*args,**kwargs)
        print("after {}() function,my ip is:".format(func.__name__),get_myip())
        return res
    return wrapper

#获取本地外网IP   
def get_myip():
    url = 'http://www.whatismyip.com.tw'
    head = {}
    #写入User Agent信息
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0"
    #创建Request对象
    req = request.Request(url, headers=head)
    #传入创建好的Request对象
    response = request.urlopen(req)
    #读取响应信息并解码
    html = response.read().decode('utf-8')
    obj=re.search('\"ip\"\:.*((\d{1,3}\.){3}.\d{1,3})',html,re.I)
    ip=obj.group().split("\"")[3]
    return ip

#使用代理爬取url内容
def agent_ip(agent_type,agent_host,url):
    proxy = {agent_type:agent_host}
    header={}
    header["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    #创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_handler)
    #添加User Agent
    #opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    req=request.Request(url=url,headers=header)
    response = request.urlopen(req)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    print(html)
    '''
    obj=re.search('\"ip\"\:.*((\d{1,3}\.){3}.\d{1,3})',html,re.I)
    print(obj.groups())
    ip=obj.group().split("\"")[3]
    return ip
    '''

if __name__ == "__main__":
    agent_type="https"
    agent_host="219.138.58.26:3128"
    url="http://www.baidu.com"
    agent_ip(agent_type,agent_host,url)