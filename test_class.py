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

class C:
    def __init__(self):
        self._a = 10
        self.__a = 20

    def test(self):
        print self.__a

if __name__ == '__main__':
    a = C()
    print a._a
    a.test()
    print a._C__a
    print a.__a
