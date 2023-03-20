# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests

def main():
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    baseurl = "http://www.hfxscw.com/"
    res = requests.get(url=baseurl, headers=head)
    res.encoding='utf-8'
    connect = res.text
    res = BeautifulSoup(connect, 'lxml')
    info = res.select('.tempWrap ul li')
    for items in info:
        detail=items.text.replace('\n', '').split(" ")
        mat = "{:15}\t{:13}\t{:15}\t{:17}"
        print(mat.format("客户或公司简称："+detail[0],"    所在地区："+detail[1],"    业务号："+detail[2],"    业务类型："+detail[3],"    业务员进展目前状态："+detail[4]))


if __name__ == '__main__':
    main()