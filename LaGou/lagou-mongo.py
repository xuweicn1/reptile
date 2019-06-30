from bs4 import BeautifulSoup
import config
import requests
import time
import pymongo
from multiprocessing import Pool

client = pymongo.MongoClient(config.MONGO_URL, 27017)
db = client[config.MONGO_DB]


def save_database(data, MONGO_TABLE):
    """数据写入mongodb"""
    if db[MONGO_TABLE].insert_one(data):
        print('保存数据库成功', data)


def parse_link(url, mongo_table):
    # url = 'https://www.lagou.com/zhaopin/Python/'
    for page in range(1, 31):
        link = '{}{}/?filterOption=3'.format(url, str(page))
        resp = requests.get(link, headers=config.head())
        if resp.status_code == 404:
            pass
        else:
            soup = BeautifulSoup(resp.text, 'lxml')

        pos_link = config.position()    # 链接
        sel = list(map(soup.select, pos_link))  # 筛选
        data = zip(*sel)  # 转置

        for position, add, release_time, money, need, company, tag, welfare in data:

            data = {
                'position': position.get_text(),
                'add': add.get_text(),
                'release_time': release_time.get_text(),
                'money': money.get_text(),
                'need': need.get_text().split('\n')[2],
                'company': company.get_text(),
                'tag': tag.get_text().replace('\n', '-'),
                'welfare': welfare.get_text()
            }
            save_database(data, mongo_table)



if __name__ == '__main__':
    t1 = time.time()
    url = 'https://www.lagou.com/zhaopin/Python/'
    parse_link(url, 'Python')
    print(time.time() - t1)
