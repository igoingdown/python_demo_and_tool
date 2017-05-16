#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
===============================================================================
author: 赵明星
desc:   基于torch实现的classification。
===============================================================================
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def mean_of_sequence():
    l = [1, 2, 3, 4, 5]
    return [(l[x] + l[x+1] + l[x + 2] + l[x+3] + l[x + 4]) / 5
            for x in range(len(l) - 4)]

if __name__ == '__main__':
    print mean_of_sequence()
