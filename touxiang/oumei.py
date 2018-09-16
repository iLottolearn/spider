import random
import urllib

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = 'https://www.woyaogexing.com/touxiang/z/nanom/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

#获取每一页的链接
def get_index():
    urllist = [base_url]
    for i in range(2,18):
        urls = base_url + 'index_' + str(i) + '.html'
        urllist.append(urls)
    return urllist
#获取每一页的数据
def get_data(url):
    driver.get(url)
    time.sleep(2)
    data = driver.page_source
    return data
#获取每页中每个头像集合的链接
def get_href(data):
    pages = []
    soup = BeautifulSoup(data,'lxml')
    hrefs = soup.find_all('a',{'class':'img'})
    for href in hrefs:
        page = href.get('href')
        pages.append(page)
    return pages
#获取图片
def get_pic(pages):
    x = 1
    url_1 = 'https://www.woyaogexing.com'
    for page in pages:
        url = url_1 + page
        time.sleep(2)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html,'lxml')
        imgs = soup.find_all('a',{'class':'swipebox'})

        print("正在下载")
        for img in imgs:
            time.sleep(round(random.uniform(1,2),2))
            src = img.get('href')
            src = 'https:' + src
            print("正在下载第{}张图片".format(x))
            urllib.request.urlretrieve(src,"D:\\pic\%s.jpg"%(x))
            x += 1


def main():
    urllist = get_index()
    for url in urllist:
        data = get_data(url)
        pages = get_href(data)
        get_pic(pages)


if __name__ == '__main__':
    main()

