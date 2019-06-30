from bs4 import BeautifulSoup
import config
import requests
import time
import pymongo
from multiprocessing import Pool
from models import Database
import threading

db = Database()


def parse_link(url):
    """内容页爬取字段"""
    # resp = requests.get(url, headers=headers, proxies=proxies)
    # headers = config.random_header()
    headers = config.head()
    print(headers)
    resp = requests.get(url, headers=headers)

    if resp.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(resp.text, 'lxml')

    pos_link = config.position()    # 链接
    sel = list(map(soup.select, pos_link))  # 筛选
    for position, region, release_time, money, need, company, tag, welfare, industry in zip(*sel):

        position = position.get_text()

        # region = region.get_text()
        city = region.get_text().split('·')[0]
        area = region.get_text().split('·')[1]
        release_time = release_time.get_text()
        money = money.get_text()
        need = need.get_text().split('\n')[2]
        company = company.get_text()
        tag = tag.get_text().replace('\n', '-')
        welfare = welfare.get_text()
        industry = industry.get_text().replace('\n', '').replace(' ', '')

        # print(position, type(position))
        # print(city, type(city))
        # print(area, type(area))
        # print(release_time, type(release_time))
        # print(money, type(money))
        # print(need, type(need))
        # print(company, type(company))
        # print(tag, type(tag))
        # print(welfare, type(welfare))
        # print(industry, type(industry))
        # print('*'*120)
        db.insert_position(position, city, area, release_time,
                           money, need, company, tag, welfare, industry)
        # thread_lock.release() #解锁


def main(url, starpage, endpage, delay):
    """主函数,多线程"""
    n = 0
    for page in range(starpage, endpage+1):
        link = '{}{}/?filterOption=3'.format(url, str(page))
        print(link)
        print('正在爬取第{}页'.format(page))
        parse_link(link)
        time.sleep(delay)
        n += 1
        print('n=', n)
        if n % 5 == 0:
            time.sleep(15)

        # 上锁
        # thread_lock.acquire()
        # t = threading.Thread(target=parse_link, args=[link])
        # t.start()
    print('采集完毕')


if __name__ == '__main__':
    # t1 = time.time()
    url = 'https://www.lagou.com/zhaopin/Python/'
    # parse_link(url, 'Python')
    # print(time.time() - t1)

    db = Database()
    db.create_lagou_position()

    main(url, 1, 30, 10)
