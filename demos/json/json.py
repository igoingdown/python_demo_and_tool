#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   测试json包的简单功能。
===============================================================================
"""

import json


def test():
    d = {'a': 10,
         'c': [20, 30]}
    json_d = json.dumps(d)
    print(json_d)
    print(json.loads(json_d))


if __name__ == '__main__':
    test()
