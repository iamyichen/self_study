# -*- coding: UTF-8 -*-
from urllib import request
from http import cookiejar
import re

#直接爬取本地外网IP
def get_myip():
    url = 'http://www.whatismyip.com.tw'
    head = {}
    #写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #创建Request对象
    req = request.Request(url, headers=head)
    #传入创建好的Request对象
    response = request.urlopen(req)
    #读取响应信息并解码
    html = response.read().decode('utf-8')
    #获取本地外网IP
    obj=re.search('\"ip\"\:.*((\d{1,3}\.){3}.\d{1,3})',html,re.I)
    ip=obj.group().split("\"")[3]
    return ip

#使用代理爬取本地wan IP
def agent_ip(agent_type,agent_host):
    # 用来爬取IP的目标网址
    url = "http://www.whatismyip.com.tw"
    # 要发送的post数据
    data = {}
    # User-Agent类型
    firefox = "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0"

    # 以下定义的两种header可二选一使用，要么使用opener传递，要么使用request传递
    # 定义opener的header
    user_agent = ("User-Agent", firefox)
    connection = ("Connection", "keep-alive")
    opener_header = [user_agent, connection]
    # 定义request的header
    request_header = {}
    request_header["User-Agent"] = firefox
    request_header["Connection"] = "keep-alive"
    # cookie保存文件
    file = "cookie.txt"
    # 代理服务器
    proxy_type = "https"
    host = "118.254.142.42:53281"
    # 初始化cookie
    cookie = cookiejar.MozillaCookieJar(filename=file)
    cookie_handler = request.HTTPCookieProcessor(cookie)
    # 初始化proxy
    proxy = {proxy_type: host}
    proxy_handler = request.ProxyHandler(proxy)
    # 初始化opener
    opener = request.build_opener(proxy_handler, cookie_handler)
    opener.addheaders = opener_header  # 此处用opener传参header
    # request.install_opener(opener)
    # 获取response
    # formdata = parse.urlencode(data).encode("utf-8")
    req = request.Request(url)  # 前面有使用opener.addheaders传参，此处不需要传递header
    response = opener.open(req)
    # 保存cookie
    cookie.save(filename=file)
    # 用response获取网页
    html = response.read().decode("utf-8")
    # 从网页获取IP
    obj = re.search('\"ip\"\:.*((\d{1,3}\.){3}.\d{1,3})', html, re.I)
    ip = obj.group().split("\"")[3]
    return ip

if __name__ == "__main__":
    #直接爬取IP很可能会被服务器屏蔽，导致爬取失败！
    #代理服务器类型
    agent_type="https"
    #代理服务器主机（IP：port）
    #若代理服务器不可用，可上http://www.xicidaili.com/网站自行选择可用代理即可
    agent_host="118.254.142.42:53281"
    #调用自定义方法获取本地外网IP
    data=agent_ip(agent_type,agent_host)
    print(data)