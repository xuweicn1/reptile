from bs4 import BeautifulSoup
import config
import requests
import time
import pymongo
from models import Database
import threading

# 设置最大线程锁为10
thread_lock = threading.BoundedSemaphore(value=2)


db = Database()

def parse_link(url):
    """内容页爬取字段"""

    # headers = config.random_header()
    headers = config.head()
    resp = requests.get(url, headers=headers)
    time.sleep(10)
    if resp.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(resp.text, 'lxml')

    pos_link = config.position()    # 链接
    sel = list(map(soup.select, pos_link))  # 筛选
    for position, region, release_time, money, need, company, tag, welfare, industry in zip(*sel):

        position = position.get_text()
        city = region.get_text().split('·')[0]
        area = region.get_text().split('·')[1]
        release_time = release_time.get_text()
        money = money.get_text()
        need = need.get_text().split('\n')[2]
        company = company.get_text()
        tag = tag.get_text().replace('\n', '-')
        welfare = welfare.get_text()
        industry = industry.get_text().replace('\n', '').replace(' ', '')
        info = [position, city, area, release_time, money, need, company, tag, welfare, industry]
        print(info)

    thread_lock.release() #解锁

def page(url, starpage, endpage):
    """获取采集页面"""
    for page in range(starpage, endpage+1):
        link = '{}{}/?filterOption=3'.format(url, str(page))
        yield link

def main(link):
    """主函数,多线程"""

    print('开始采集...')
    parse_link(link)
    # time.sleep(10)
    # print('采集完毕!!!')


if __name__ == '__main__':

    t1 = time.time()
    # pool = Pool(processes=10)
    url = 'https://www.lagou.com/zhaopin/Python/'
    link = (link for link in page(url, 1, 10))

    n = 0
    for link in page(url, 1, 10):
        n += 1
        print('正在下载第{}页'.format(n))
        thread_lock.acquire()
        t = threading.Thread(target=main, args=(link,))
        t.start()


    print(time.time() - t1)


 