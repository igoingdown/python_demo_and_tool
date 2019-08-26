#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   测试python类结构
===============================================================================
"""


class C:
    def __init__(self):
        self._a = 10
        self.__a = 20

    def test(self):
        print(self.__a)


if __name__ == '__main__':
    a = C()
    print(a._a)
    a.test()
    print(a._C__a)
    print("error should occured")
    print(a.__a)
