#!/usr/bin/env python3

"""
===============================================================================
author: 赵明星
desc:   北邮校园网自动登录。
===============================================================================
"""

import urllib2
import urllib
import re


class Loginer():
    def __init__(self, username, password):
        self.loginUrl = 'http://10.3.8.211/'
        self.username = username
        self.password = password

    def login(self):
        postdata = {
                   'DDDDD': self.username,
                   'upass': self.password,
                   'savePWD': 0,
                   '0MKKey': ''
                   }
        postdata = urllib.urlencode(postdata)
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)
        result = urllib2.build_opener().open(myRequest).read()
        unicodePage = result.decode('gb2312')
        msg = re.findall('<title>(.*?)</title>', unicodePage)[0]
        if msg.encode('utf-8') == '登录成功窗':
            print('账号：', self.username, '登录成功！')
        else:
            print('账号：', self.username, '登录失败！')


def main():
    userID = "YOUR STUDENT CARD ID"
    loginer = Loginer(userID, "YOUR PASSWORD")
    loginer.login()


if __name__ == '__main__':
    main()
