from bs4 import BeautifulSoup
from urllib import request
import re
import os
import sys

def get_chapter(url):
    header = {}
    header["User-Agent"] = "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0"
    req = request.Request(url=url, headers=header)
    response = request.urlopen(req)
    html = response.read().decode("gbk")
    soup = BeautifulSoup(html, "lxml")
    chapter_content = soup.find(name="div", attrs={"id": "content", "class": "showtxt"}, )
    chapter_title = soup.find(name="div", attrs={"class": "content"})
    content = str(chapter_content).replace("<br/><br/>", "\n").replace("\xa0", "")
    story = BeautifulSoup(content, "lxml")
    title = BeautifulSoup(str(chapter_title), "lxml")
    name = title.find(name="h1")
    return (name.string, story.text)


def chapter_save(file_path, filename, chapter):
    title = chapter[0]
    content = chapter[1]
    os.makedirs(file_path, exist_ok=True)
    file = open(file_path + filename, "a")
    file.write(title + "\n\n" + content + "\n\n")
    file.close()

def get_links(start=0,step=100):
    url="http://www.biqukan.com/1_1094"
    header = {}
    header["User-Agent"] = "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0"
    req=request.Request(url)
    response=request.urlopen(req)
    html=response.read().decode("gbk")
    links_soup=BeautifulSoup(html,"lxml")
    links_list=links_soup.find_all("div",attrs={"class":"listmain"})
    links=BeautifulSoup(str(links_list),"lxml")
    begin=False
    for child in links.dl.children:
        if child!="\n":
            if re.search(".*第一章.*",child.string):
                begin=True
            if begin==True and child.a!=None and re.search(".*第.*章.*",child.string):
                chapter_url="http://www.biqukan.com"+child.a["href"]
                chapter_name=child.string
                yield (chapter_url,chapter_name)

def save_all(file_path,file_name):
    for (url,name) in get_links():
        chapter=get_chapter(url)
        print("正在保存{}。。。\n".format(name))
        chapter_save(file_path=file_path,filename=file_name,chapter=chapter)
        print("成功保存{}\n".format(name))

def main():
    file_path="e:/story/"
    file_name="一念永恒.txt"
    save_all(file_path,file_name)

if __name__ == '__main__':
    main()
