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


# raw_salary = society_insurance + base_allowance + tax + taxed_salary
# base_raw_salary 表示较为固定的税前月薪
# actual_raw_salary 表示实际的一个月的税前月薪，适用于每月税前薪资波动的场景

class Calculator(object):
    def __init__(self, base_raw_salary, society_insurance, registered_house_rent):
        self.base_raw_salary = base_raw_salary
        self.society_insurance = society_insurance
        self.registered_house_rent = registered_house_rent
        self.house_rent_allowance = 1000.0
        self.base_allowance = 5000.0

    def calculate_Nth_month_salary(self, n):
        before_tax_income_sum = self.base_raw_salary * n - self.society_insurance * n - self.base_allowance * n
        if self.registered_house_rent:
            before_tax_income_sum -= self.house_rent_allowance * n
        # 查dict，找出税率和速算扣除数
        rate, reduce_num = find_tax_range(before_tax_income_sum)
        tax_sum = before_tax_income_sum * rate - reduce_num
        return tax_sum

    def calculate_next_month_salary(self, previous_actual_raw_salary_list, tax_record_list):

        before_tax_income_sum = sum(previous_actual_raw_salary_list, self.base_raw_salary) - (self.society_insurance + self.base_allowance) * (len(previous_actual_raw_salary_list) + 1)
        if self.registered_house_rent:
            before_tax_income_sum -= self.house_rent_allowance * (1 + len(previous_actual_raw_salary_list))
        # 查dict，找出税率和速算扣除数
        rate, reduce_num = find_tax_range(before_tax_income_sum)
        tax_sum = before_tax_income_sum * rate - reduce_num
        return -sum(tax_record_list, -tax_sum)

    def print_annual_income_curve(self):
        last_tax_sum = 0.0
        for i in range(1, 13):
            # 计算每月的收入
            cur_tax_sum = self.calculate_Nth_month_salary(i)
            print(cur_tax_sum - last_tax_sum)
            last_tax_sum = cur_tax_sum


if __name__ == "__main__":
    c = Calculator(36000, 6000, False)
    c.print_annual_income_curve()
