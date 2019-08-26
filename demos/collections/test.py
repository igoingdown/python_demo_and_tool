#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   测试collections包的简单功能。
===============================================================================
"""

from collections import Counter


def foo():
    s = "here we go"
    word_counter = Counter()
    for w in s.split():
        word_counter[w] += 1
    for k, v in word_counter.items():
        print(k, v)


if __name__ == '__main__':
    foo()
