#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
===============================================================================
author: 赵明星
desc:   抓取有意思的图片。
===============================================================================
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import os
import os.path
import urllib
import random
from bs4 import BeautifulSoup


class LittleCrawler(object):
    def __init__(self, original_url):
        self.image_url_list = []
        self.soup = None
        self.url = original_url

    def get_soup(self):
        my_headers = [
            'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 ' +
                '(KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
            'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2;\
                    Trident/4.0; .NET CLR 1.1.4322; '
                    '.NET CLR 2.0.50727;\
                    .NET4.0E; .NET CLR 3.0.4506.2152; \
                    .NET CLR 3.5.30729; .NET4.0C)',
            'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 \
                    Version/11.50',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) \
                    AppleWebKit/533.21.1 (KHTML, like Gecko)\
                    Version/5.0.5 Safari/533.21.1',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; \
                    Trident/4.0; .NET CLR 2.0.50727;\
                    .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; \
                    .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']

        header = {"User-Agent": random.choice(my_headers)}
        req = urllib2.Request(self.url, headers=header)
        html = urllib2.urlopen(req).read()
        self.soup = BeautifulSoup(html)

    def get_pages(self):
        result = self.soup.find_all('a', class_="thumbnail")
        for image_url in result:
            self.image_url_list.append(image_url['href'])

    def get_image(self):
        self.get_soup()
        self.get_pages()
        dir_name = 'MeiZiTu'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        else:
            pass
        for i in xrange(len(self.image_url_list)):
            file_name = os.path.join(dir_name, str(i)+'.jpg')
            if not os.path.exists(file_name):
                urllib.urlretrieve(self.image_url_list[i], file_name)
            else:
                pass

if __name__ == '__main__':
    url = 'http://www.pink18.com/'
    crawler = LittleCrawler(url)
    crawler.get_image()
