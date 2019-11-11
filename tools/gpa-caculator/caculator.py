#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   计算本科GPA。
===============================================================================
"""

import xlrd


class Calculator(object):
    def __init__(self, file_name):
        self.fileName = file_name

    def calcuate(self):
        data = xlrd.open_workbook(self.fileName)
        table = data.sheets()[0]
        weight_list = table.col_values(4)
        score_list = table.col_values(6)
        gpa = 0.0
        weight = 0.0
        for i in range(len(score_list)):
            gpa += float(score_list[i]) * weight_list[i]
            weight += weight_list[i]
        print("total GPA is:", gpa/weight)


if __name__ == "__main__":
    calculator = Calculator('scores.xlsx')
    calculator.calcuate()
