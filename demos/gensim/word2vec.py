#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   利用gensim实现基本的word2vec并训练词向量。
===============================================================================
"""

import gensim
import jieba
import os


def main():
    sentence_list = []
    for file in os.listdir("weibo_texts"):
        path = os.path.join("weibo_texts", file)
        with open(path) as f:
            for line in f:
                sentence = jieba.cut(line)
                words = [x for x in sentence]
                sentence_list.append(words)

    model = gensim.models.Word2Vec(sentence_list, min_count=1)
    model.train(sentence_list)
    model.save('my_model')


if __name__ == '__main__':
    main()
