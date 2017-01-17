#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
===============================================================================
author: 赵明星
desc:   从进程描述文件中取出特定进程的pid并写入新的文件。
===============================================================================
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open("process.out", "r") as f:
	with open("python_pids.out", "w") as f_w:
		for line in f:
			words = [x.strip() for x in line.split()]
			if len(words) > 1 and words[1] == \
				"ls_sub_rel_test_data_multi_thread.py":
				print >> f_w, words[0]

