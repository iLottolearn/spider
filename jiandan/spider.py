import urllib

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

base_url = 'http://jandan.net/pic/'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
driver = webdriver.Chrome()




def get_page():
    response = requests.get(base_url)
    html = response.text
    urllist = []
    soup = BeautifulSoup(html,'lxml')
    allpage = soup.find('span',{'class':'current-comment-page'}).get_text()[1:-1]
    for i in range(1,int(allpage)+1):
        allurl = base_url + 'page-' + str(i)
        urllist.append(allurl)
    return urllist


def find_pic(urllist):
    x = 1
    for url in urllist:
        print('正在访问{}'.format(url))
        try:
            driver.get(url)
            driver.implicitly_wait(30)
            data = driver.page_source
            soup = BeautifulSoup(data,'lxml')
            hrefs = soup.find_all('a',{'class':'view_img_link'})
        except:
            print('访问异常')


        print('开始下载')

        for href in hrefs:
            img = href.get('href')
            img = "http:"+ img
            print('正在下载第{}张图片'.format(x))
            urllib.request.urlretrieve(img,"D:\\pic\%s.jpg"%(x))
            x += 1


def main():
    urllist = get_page()
    find_pic(urllist)



if __name__ == '__main__':
    main()