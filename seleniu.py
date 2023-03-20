# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

#阿越的测试
def ayuetest():
    browser = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
    # executable_path来指定chromedirver路路径
    browser.get("https://data.eastmoney.com/bbsj/zcfz/688586.html")
    txt=browser.page_source
    print("网站源码:"+str(txt))

#百度的测试
def seleniumTest():
    browser = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
    # executable_path来指定chromedirver路路径
    browser.get("https://www.baidu.com")
    # browser.find_element()

    browser.find_element(By.CLASS_NAME, "s-top-login-btn").click()
    # browser.find_element_by_class_name("s-top-login-btn").click()

    time.sleep(1)
    WebDriverWait(browser, 1, poll_frequency=0.5, ignored_exceptions=None)

    # 输入账号
    browser.find_element(By.ID, "TANGRAM__PSP_11__userName").click()
    browser.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("944057541@qq.com")

    # 输入密码
    browser.find_element(By.ID, "TANGRAM__PSP_11__password").click()
    browser.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("zhangyi0906")

    # 点击登录
    browser.find_element(By.ID, "TANGRAM__PSP_11__submit").click()

    time.sleep(10)
if __name__ == '__main__':
    ayuetest()

