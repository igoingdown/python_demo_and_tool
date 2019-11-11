#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   计算新个税下的个人收入。
===============================================================================
"""


# a dict for limit to tax rage and reduce num
d = {
    36000.0: (0.03, 0),
    144000.0: (0.1, 2520),
    300000.0: (0.2, 16920),
    420000.0: (0.25, 31920),
    660000.0: (0.3, 52920),
    960000.0: (0.35, 85920),
    100000000000000000: (0.45, 181920)
}


def find_tax_range(before_tax_income_sum):
    for k, v in d.items():
        pass
        if before_tax_income_sum > k:
            continue
        return v


class Calculator(object):
    def __init__(self, base_salary, society_insurance,
                 no_tax_base_income, registered_house_rent):
        self.base_salary = base_salary
        self.society_insurance = society_insurance
        self.no_tax_base_income = no_tax_base_income
        self.registered_house_rent = registered_house_rent

    def calculate_Nth_month_salary(self, n):
        before_tax_income_sum = self.base_salary * n - self.society_insurance * n - 5000.0 * n
        if self.registered_house_rent:
            before_tax_income_sum -= 1000.0 * n
        # 查dict，找出税率和速算扣除数
        rate, reduce_num = find_tax_range(before_tax_income_sum)
        tax_sum = before_tax_income_sum * rate - reduce_num
        return tax_sum

    def calculate_next_month_salary(self, salary_totals, tax_records):
        before_tax_income_sum = sum(salary_totals, self.base_salary) - (self.society_insurance + 5000.0) * (len(salary_totals) + 1)
        if self.registered_house_rent:
            before_tax_income_sum -= 1000.0 * (1 + len(salary_totals))
        # 查dict，找出税率和速算扣除数
        rate, reduce_num = find_tax_range(before_tax_income_sum)
        tax_sum = before_tax_income_sum * rate - reduce_num
        return -sum(tax_records, -tax_sum)

    def print_annual_income_curve(self):
        last_tax_sum = 0.0
        for i in range(13):
            if i == 0:
                continue
            # 计算每月的收入
            cur_tax_sum = self.calculate_Nth_month_salary(i)
            print(cur_tax_sum - last_tax_sum)
            last_tax_sum = cur_tax_sum


if __name__ == "__main__":
    pass
