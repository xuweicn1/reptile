import random

MONGO_URL = 'localhost'
# 数据库名
MONGO_DB = 'lagou'


def head():
    # headers = {
    #     'Cookie': 'user_trace_token=20170603115043-d0c257a054ee44f99177a3540d44dda1; LGUID=20170603115044-d1e2b4d1-480f-11e7-96cf-525400f775ce; JSESSIONID=ABAAABAAAGHAABHAA8050BE2E1D33E6C2A80E370FE9167B; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; login=false; unick=""; _putrc=""; _ga=GA1.2.922290439.1496461627; X_HTTP_TOKEN=3876430f68ebc0ae0b8fac6c9f163d45; _ga=GA1.3.922290439.1496461627; LGSID=20170720174323-df1d6e50-6d2f-11e7-ac93-5254005c3644; LGRID=20170720174450-12fc5214-6d30-11e7-b32f-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500541369; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500543655',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    # }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    # localhost google
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    return headers


def position():
    """配置div字段位置"""
    positions = 'ul > li > div.list_item_top > div.position > div.p_top > a > h3'
    adds = 'ul > li > div.list_item_top > div.position > div.p_top > a > span > em'
    publishs = 'ul > li > div.list_item_top > div.position > div.p_top > span'
    moneys = 'ul > li > div.list_item_top > div.position > div.p_bot > div > span'
    needs = 'ul > li > div.list_item_top > div.position > div.p_bot > div'
    companys = "ul > li > div.list_item_top > div.company > div.company_name > a"
    tags = 'ul > li > div.list_item_bot > div.li_b_l'
    fulis = 'ul > li > div.list_item_bot > div.li_b_r'
    industry = "ul > li> div.list_item_top > div.company > div.industry"
    return positions, adds, publishs, moneys, needs, companys, tags, fulis, industry


def random_header():
    """返回随机的header"""
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    ]
    user_agent = random.choice(user_agent_list)
    headers = {
        'User-Agent': user_agent,
        'Connection': 'keep-alive'
    }
    return headers


def proxy_list():
    """返回随机的IP地址"""
    proxy_list = [
        'http://140.224.76.21:808',
        'http://60.178.14.90:8081',
        'http://121.232.146.13:9000',
    ]
    proxy_ip = random.choice(proxy_list)
    proxies = {
        'http': proxy_ip,
        'https': proxy_ip,
    }

    return proxies
