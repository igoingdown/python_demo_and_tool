#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   测试tqdm包的简单功能。
===============================================================================
"""

from tqdm import tqdm
from tqdm import tgrange
from time import sleep


def foo():
    for i in tqdm(range(10)):
        sleep(0.1)
        print("-" * 100, "*" * 10, "-" * 100)

    for i in tgrange(10):
        sleep(1.0)
        print('*' * 10)


if __name__ == '__main__':
    foo()
