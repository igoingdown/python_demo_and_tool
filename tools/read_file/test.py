#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   读文件并进行统计
===============================================================================
"""


def read_f():
    s = set()
    with open("/Users/zhaomingxing/Desktop/hive_tables.o") as f:
        for line in f:
            if f != "":
                s.add(line)
    for line in s:
        print(line)


if __name__ == "__main__":
    read_f()
