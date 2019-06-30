import requests
import threading
import urllib.parse
import json
import time
# 设置最大线程锁为10
thread_lock = threading.BoundedSemaphore(value=10)


def get_page(url):
    """通过url获取数据"""
    data = requests.get(url).text
    page = json.loads(data)
    return page


def page_from_duitang(label):
    """取页内容列表"""
    pages = []
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000'
    label = urllib.parse.quote(label)  # 中文转url编码
    for index in range(0, 3000, 50):
        u = url.format(label, index)
        page = get_page(u)
        object_list = page['data']['object_list']
        pages.append(object_list)
    return pages


def pic_urls_from_page(pages):
    """获取图片地址列表"""
    pic_urls = []
    for object_list in pages:
        for v in object_list:
            if v['photo']['path']:
                pic_urls.append(v['photo']['path'])
    return pic_urls


def downloa_pics(url, n):
    """从指定地址下载图片"""
    r = requests.get(url)
    path = 'temp/' + str(n) + '.jpg'
    with open(path, 'wb') as f:
        f.write(r.content)
    thread_lock.release()  # 下载图片后解锁


def main(label):
    """主函数"""
    pages = page_from_duitang(label)
    pic_urls = pic_urls_from_page(pages)
    n = 0
    for url in pic_urls:
        n += 1
        print('正在下载第{}张图片'.format(n))
        # 上锁
        thread_lock.acquire()
        t = threading.Thread(target=downloa_pics, args=(url, n))
        t.start()


if __name__ == "__main__":

    t1 = time.time()
    main('校花')
    print(time.time() - t1)
