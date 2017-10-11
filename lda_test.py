#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
===============================================================================
author: 赵明星
desc:   从进程描述文件中取出特定进程的pid并写入新的文件。
===============================================================================
"""

import numpy as np
import lda
import lda.datasets

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()

print "X.shape = {}".format(X.shape)
print "X.sum = {}".format(X.sum())

m = lda.LDA()
model = lda.LDA(n_topics=20, n_iter=1000, random_state=1)
model.fit(X)

topic_word = model.topic_word_
n_top_word = 8
for i, topic_dist in enumerate(topic_word):
	topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_word+1):-1]
	print "topic {0}:{1}".format(i, ''.join(topic_words))
