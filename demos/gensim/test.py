#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   测试gensim包的简单功能。
===============================================================================
"""

import gensim
import jieba


def foo():
    lines = []
    with open("weibo_texts/test.txt") as f:
        for line in f:
            lines.append(jieba.cut(line))
    d = gensim.corpora.Dictionary(lines)
    for word, index in d.token2id.iteritems():
        print(word, index)


if __name__ == '__main__':
    foo()
