import csv

import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://www.liepin.com/zhaopin/?ckid=c857542728a83251&fromSearchBtn=2&init=-1&sfrom=click-pc_homepage-centre_searchbox-search_new&dqs=050020&flushckid=1&key=python&headckid=c857542728a83251&d_pageSize=40&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_headId=73ef19976707c22089247024b5f2ae9b&d_ckId=73ef19976707c22089247024b5f2ae9b&d_sfrom=search_fp&d_curpage='
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

#取得html
def get_html(url):
    try:
        response = requests.get(url,headers=headers)
        html = response.text
        if response.status_code == 200:
            return html
    except ConnectionError:
        return get_html(url)

#解析每页的招聘信息
def parse_page(html):
    alljobs = []
    soup = BeautifulSoup(html,'lxml')
    jobs = soup.find_all('div',{'class':'sojob-item-main clearfix'})
    for job in jobs:
        title = job.div.h3.a.text.strip()
        link = job.div.h3.a['href']
        info = job.div.p['title']
        company_p = job.find('p',{'class':'company-name'})
        company = company_p.a.text
        alljobs.append([title,link,info,company])
    return alljobs
#取得每页url
def get_url():
    urllist = []
    for i in range(65):
        url = base_url + str(i)
        urllist.append(url)
    return urllist

def main():
    x = 1
    urllist = get_url()
    for url in urllist:
        html = get_html(url)
        alljobs = parse_page(html)
        print("正在获取第{}页".format(x))
        with open('liepin.csv','a',encoding='utf=8') as f:
            writer = csv.writer(f)
            writer.writerow(['职位','链接','信息','公司名称'])
            for row in alljobs:
                writer.writerow(row)
        x += 1
    print("获取完成")



if __name__ == '__main__':
    main()
