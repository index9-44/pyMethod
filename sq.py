# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

#mysql 的实验
import datetime
import pymysql
from bs4 import BeautifulSoup
import requests
import time
movieList = set()            #设置一个获取所有电影的列表
db = pymysql.connect(host="116.205.241.124", user="test1", password="zhangyi0906", database="douban")
# db = pymysql.connect(host="localhost", user="root", password="123456", database="douban")
#爬取豆瓣top250教程,输入index下标，来爬取对应的数据
def getMovie(index,times):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    baseurl = "https://movie.douban.com/top250?start="+str(index)
    res = requests.get(url=baseurl, headers=head)
    connect = res.text
    res = BeautifulSoup(connect, 'lxml')
    video = res.select('.grid_view li .info .hd')
    for movies in video:
        index+=1
        currentMovie = (index,movies.select('.title')[0].text, times, datetime.datetime.now(), datetime.datetime.now())
        movieList.add(currentMovie)


#把查询到的数据插入数据库
def insertMysql():
    # 创建一个数据库连接对象，指定主机名，用户名，密码和数据库名
    #db = pymysql.connect(host="116.205.241.124", user="test1", password="zhangyi0906", database="douban")
    # 创建一个游标对象，用来执行SQL语句
    cursor = db.cursor()
    # 定义要执行的SQL语句
    sql = "INSERT INTO top250 (top,m_name, times,create_time,update_time) VALUES (%s,%s,%s,%s,%s)"
    # 使用游标对象执行SQL语句，并传入参数
    cursor.executemany(sql, movieList)
    # 提交事务，使数据生效
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()

#查询top数据库最后一条数据，获取上个版本的日期顺序,返回最后一条数据的上个版本的日期顺序
def searchLastData():
    # 显示数据库表最后一个数据
    cursor = db.cursor()
    query = "select * from {0} order by {1} desc limit 1;".format("top250", "uid")
    cursor.execute(query)
    record_last = cursor.fetchone()
    db.commit()
    if(record_last is None):
        return 0
    else:
        return record_last[2]

#爬取豆瓣top250的数据至数据库
def doubantop250():
    times=searchLastData()+1
    index = 0
    for i in range(10):
        getMovie(index,times)
        index += 25
        time.sleep(5)
    insertMysql()

#mysql查询通用接口
def searchMysql(query):
    cursor = db.cursor()
    cursor.execute(query)
    getData = cursor.fetchall()
    db.commit()
    return getData

#向数据库中查询本次记录与上次记录的情况，输出结果
def topDifference():
    upMovieList=set()               #排名提升
    downMovieList = set()           #排名下降
    # newMovieList=set()              #新电影上榜top250
    # keepAwawMoviveList=set()        #跌落榜单
    query1 = "select m_name,top from {0} where times={1};".format("top250", searchLastData())
    query2 = "select m_name,top from {0} where times={1};".format("top250", searchLastData()-1)
    FirstMovieList=searchMysql(query1)          #本周的电影top250排行榜
    SecondMovieList=searchMysql(query2)         #上一周电影top250排行榜
    #双层循环，首先根据本期的电影排名列表，一个一个遍历（暂时缺少跌落榜单的功能）
    for FirstIndex, FirstMovie in enumerate(FirstMovieList):
        for SecondIndex,SecondMovie in enumerate(SecondMovieList):
            if FirstMovie[0]==SecondMovie[0]:            #如果查询到了本部电影
                if FirstMovie[1] > SecondMovie[1]:
                    downMovieList.add(FirstMovie)
                    continue
                elif FirstMovie[1]<SecondMovie[1]:
                    upMovieList.add(FirstMovie)
                    continue
    print("本周新上新的电影："+str(list((filter(lambda t: t[0] not in {t[0] for t in SecondMovieList}, FirstMovieList)))))
    print("本周新下榜的电影："+str(list((filter(lambda t: t[0] not in {t[0] for t in FirstMovieList}, SecondMovieList)))))


    print("本周有"+str(len(upMovieList))+"排名上升，本周排名上升的电影："+str(upMovieList))
    print("本周有"+str(len(downMovieList))+"排名下降，本周排名下降的电影："+str(downMovieList))


if __name__ == '__main__':
    #爬取豆瓣top250的数据至数据库
    #doubantop250()
    topDifference()






