import re
from http import cookiejar
from urllib import parse
from urllib import request


def main():
    url="http://www.whatismyip.com.tw"
    #url="http://www.baidu.com"
    data={}
    firefox="Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0"
    user_agent=("User_Agent",firefox)
    connection=("Connection","keep-alive")
    file="cookie.txt"
    proxy_type="http"
    host="60.191.134.165:9999"

    #初始化cookie
    cookie=cookiejar.MozillaCookieJar(filename=file)
    cookie_handler=request.HTTPCookieProcessor(cookie)
    #初始化proxy
    proxy = {proxy_type:host}
    proxy_handler=request.ProxyHandler(proxy)
    #初始化opener
    opener=request.build_opener(proxy_handler,cookie_handler)
    opener.addheaders=[user_agent,connection]
    #获取response
    formdata = parse.urlencode(data).encode("utf-8")
    request.install_opener(opener)
    req=request.Request(url,formdata)
    response=request.urlopen(req)
    #response=opener.open(url)
    #保存cookie
    cookie.save(filename=file)
    
    print(response.getcode())
    print(response.info())
    print(response.geturl())
    
    #用response获取网页
    html=response.read().decode("utf-8")
    # 从网页获取IP
    obj = re.search('\"ip\"\:.*((\d{1,3}\.){3}.\d{1,3})', html, re.I)
    ip = obj.group().split("\"")[3]
if __name__ == '__main__':
    main()