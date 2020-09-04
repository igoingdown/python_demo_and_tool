#!/usr/bin/env python3

"""
===============================================================================
author: 赵明星
desc:   热度和新鲜度分计算
===============================================================================
"""

import math
import datetime


def compare(a, b):
    if a > b:
        return 1
    return -1


def diff_rate(a, b, divisor):
    return math.log(1 + abs(a - b) / divisor)


if __name__ == "__main__":
    read0, read1, read2, read3 = 109439,101719,96046,96735
    group0, group1, group2, group3 = 6, 6, 6,6
    score = 0.5 * (
    1.0 * (
        compare(read0, read1) * diff_rate(read0, read1, 1000)
        + 0.77 * compare(read1, read2) * diff_rate(read1, read2, 1000)
        + 0.33 * compare(read2, read3) * diff_rate(read2, read3, 1000)
    )
    + 2.0 * (
        compare(group0, group1) * diff_rate(group0, group1, 10)
        + 0.77 * compare(group1, group2) * diff_rate(group1, group2, 10)
        + 0.33 * compare(group2, group3) * diff_rate(group2, group3, 10)
    )
)
    print(score)
    print(datetime.datetime.today())