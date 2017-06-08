#!/usr/bin/python
# -*- coding:utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
===============================================================================
author: 赵明星
desc:   从进程描述文件中取出特定进程的pid并写入新的文件。
===============================================================================
"""

import json


def test():
    d = {'a': 10,
         'c': [20, 30]}
    json_d = json.dumps(d)
    print json_d
    print json.loads(json_d)

if __name__ == '__main__':
    test()

