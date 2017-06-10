#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
===============================================================================
author: 宋佳明
desc:   word2vec模型的小demo。
===============================================================================
"""


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import gensim
import jieba
import os

def main():
    sentence_list = []
    for file in os.listdir("weibo_texts"):
        print file
        path = os.path.join("weibo_texts", file)
        print path
        with open(path) as f:
            for line in f:
                sentence = jieba.cut(line)
                words = [x for x in sentence]
                # print words
                print words
                sentence_list.append(words)
                # for word in words:
                #     print word
                print "-" * 100

    model = gensim.models.Word2Vec(sentence_list, min_count=1)
    model.train(sentence_list)
    print len(model.wv[u'之一'])
    model.save('my_model')



if __name__ == '__main__':
    main()



