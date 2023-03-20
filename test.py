# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
def t1():
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    baseurl = "https://movie.douban.com/top250?start=0"
    res = requests.get(url=baseurl, headers=head,timeout=5)
    connect = res.text
    res = BeautifulSoup(connect, 'lxml')
    print("获取的内容："+str(res))


if __name__ == '__main__':
    # douban()
    t1()