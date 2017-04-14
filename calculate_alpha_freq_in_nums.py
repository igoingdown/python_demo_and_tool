#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
===============================================================================
author: 赵明星
desc:   查看每个数字对应的英文单词中的字母。
===============================================================================
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    l = ["zero", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine"]

    alpha2words = {}
    for n in l:
        for c in n:
            if c not in alpha2words:
                alpha2words[c] = []
            alpha2words[c].append(n)

    sorted(alpha2words.iteritems(), key=lambda d: len(d[1]))
    for k, v in alpha2words.iteritems():
        print k, v

    dict2list = alpha2words.iteritems()
    print dict2list
    for x in dict2list:
        print x[0], x[1]

    res = sorted(dict2list, key=lambda d: len(d[1]))
    for x in res:
        print x[0], ": ", x[1]

if __name__ == '__main__':
    main()