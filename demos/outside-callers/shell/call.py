#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   测试调用shell脚本。
===============================================================================
"""


import subprocess


def foo():
    subprocess.call("./test.sh", shell=True)


if __name__ == '__main__':
    foo()
