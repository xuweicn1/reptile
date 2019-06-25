import requests
import urllib.parse
import threading
import time
# 设置最大线程锁为10
thread_lock = threading.BoundedSemaphore(value=10)


def get_page(url):
    """通过url获取数据"""
    response = requests.get(url)
    page = response.content.decode()  # byte to str
    return page


def page_from_duitang(label):
    """取页面"""
    pages = []
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000'
    label = urllib.parse.quote(label)  # 中文转url编码
    for index in range(0, 3000, 50):
        u = url.format(label, index)
        page = get_page(u)
        pages.append(page)
    return pages


def findall_in_page(page, startpart, endpart):
    """截取图片地址"""
    all_strings = []
    end = 0
    while page.find(startpart, end) != -1:
        start = page.find(startpart, end) + len(startpart)
        end = page.find(endpart, start)
        line = page[start:end]
        all_strings.append(line)
    return all_strings


def pic_urls_from_page(pages):
    """图片链接列表"""
    pic_urls = []
    for page in pages:
        urls = findall_in_page(page, 'path":"', '"')
        pic_urls.extend(urls)  # 将列表元素加入另外一个列表之后
    return pic_urls


def downloa_pics(url, n):
    """文件夹/01.jpg"""
    r = requests.get(url)
    path = 'tmp/' + str(n) + '.jpg'
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


if __name__ == '__main__':

    t1 = time.time()
    main('校花')
    print(time.time() - t1)
