#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   从进程描述文件中取出特定进程的pid并写入新的文件。
===============================================================================
"""


def pids_for_process_name(process_name):
    res = []
    with open("process.out", "r") as f:
        for line in f:
            words = [x.strip() for x in line.split()]
            if len(words) > 1 and words[1] == process_name:
                res.append(words[0])
    return res


if __name__ == "__main__":
    with open("python_pids.out", "w") as f_w:
        for pid in pids_for_process_name("ls_sub_rel_test_data_multi_thread.py"):
            print >> f_w, pid
