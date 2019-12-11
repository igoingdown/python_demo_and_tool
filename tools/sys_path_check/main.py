#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   查一下本地python是如何找包的。
===============================================================================
"""


import pprint
import sys


def check():
    pprint.pprint(sys.path)


if __name__ == "__main__":
    check()
