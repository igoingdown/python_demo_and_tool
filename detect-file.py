#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


"""
===============================================================================
author: 赵明星
desc:   我们一起来抓阄。
===============================================================================
"""

def main():
    count = 0
    with open("/Users/zhaomingxing/Desktop/describe.txt") as f:
        for line in f:
            split_res = line.split("\t")
            if len(split_res) != 9:
                print line
            count += 1

    print count


if __name__ == '__main__':
    main()
