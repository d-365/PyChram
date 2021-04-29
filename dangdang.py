import os

import requests
import re
import json


class book_rank:
    """
    新书畅销榜7日：http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-recent7-0-0-1-1
    新书畅销榜30日：http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-recent30-0-0-1-1
    图书畅销榜7日：http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-2-1
    图书畅销榜30日：http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-2-1
    """
    pass


def request_dang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


# 解析保存数据
def parse_response(html, textName):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?class="name".*?title="(.*?)">.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    dict_list = {}
    for item in items:
        # 打印一下 查看結果
        print(item)
        dict_list['range'] = item[0],
        dict_list['title'] = item[1],
        dict_list['author'] = item[2],
        dict_list['hot_num'] = item[3],
        dict_list['price'] = item[4]
        path = r'C:\Users\Administrator\Desktop\%s.txt' % textName
        with open(path, 'a+', encoding='UTF-8') as f:
            f.write(json.dumps(dict_list, ensure_ascii=False) + '\n')


def main(page):
    # 好评榜
    # url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'+str(page)
    # 新书畅销榜7日：
    url = 'http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-recent7-0-0-1-' + str(page)

    html = request_dang(url)
    parse_response(html, 'good')


# 实现翻页
if __name__ == "__main__":
    for i in range(1, 3):
        main(i)
