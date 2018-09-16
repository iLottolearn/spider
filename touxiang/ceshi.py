from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.baidu.com'
url1 = 'https://www.sogou.com'
driver.get(url)
driver.get(url1)
