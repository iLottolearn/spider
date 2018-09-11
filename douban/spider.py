import csv
import re
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
}

base_url = 'https://book.douban.com/top250?'

def get_html(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return get_html(url)
#获得url，并得到html
def get_index(start):
    data = {
        'start':start
    }
    starts = urlencode(data)
    url = base_url + starts
    html = get_html(url)
    return html
#解析网页内容
def parse_page(html):
    tables = []
    soup = BeautifulSoup(html,'lxml')
    table = soup.find_all('table',{'width':'100%'})
    for item in table:
        title = item.div.a.text.strip()
        r_title = title.replace('\n','').replace(' ','')
        link = item.div.a['href']
        info = item.p.text
        score = item.find('span',{'class':'rating_nums'}).text
        number = item.find('span',{'class':'pl'}).text.replace('\n','').replace(' ','')
        if item.find('span',{'class':'inq'}):
            quote = item.find('span',{'class':'inq'}).text
        else:
            quote = 'no description'
        tables.append([r_title,link,info,score,number,quote])
    return tables


def main():
    for start in range(0,225,25):
        html = get_index(start)
        tables = parse_page(html)
        print(tables)
        # 保存数据csv
        with open('douban.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['书名', '链接', '信息', '评分', '评价人数', '描述'])
            for row in tables:
                writer.writerow(row)




if __name__ == '__main__':
    main()

