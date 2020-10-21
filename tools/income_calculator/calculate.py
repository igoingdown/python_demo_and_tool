#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   计算新个税下的个人收入。
===============================================================================
"""

from tools.income_calculator.const import *
import math

def find_tax_range(before_tax_income_sum):
    for k, v in salary_tax_rate_dict.items():
        pass
        if before_tax_income_sum > k:
            continue
        return v


class Insurance(object):
    def __init__(self, rate, min_base, max_base, fee_base):
        self.rate = rate
        self.max_base = max_base
        self.min_base = min_base
        self.fee_base = fee_base

    def get_fee(self, base):
        base = max(min(base, self.max_base), self.min_base)
        fee = base * self.rate
        fee += self.fee_base
        return fee


class Allowance(object):
    def __init__(self, base_fee, total_fee):
        self.base_fee = base_fee
        self.total_fee = total_fee

    def get_fee(self, i):
        if i * self.base_fee <= self.total_fee:
            return self.base_fee
        else:
            return 0

# raw_salary: 当月税前月薪
# last_year_average_raw_salary: 去年平均月薪，每年7月更新
# housing_fund: 公积金
# pension: 养老保险
# unemployment_insurance: 失业保险
# housing_fund_fee(公积金总数) = last_year_average_raw_salary * housing_fund_rage
# taxed_salary = raw_salary - insurance_fee - housing_fund_fee - tax
# base_tax_free_salary: 每月免税金额,每月￥5000
# tax_free_salary(每月实际免税收入) = base_tax_free_salary + tax_free_allowance
# tax_free_allowance: 免税津贴,如租房个税减免
# tax_free_house_rent_allowance: 租房个税减免金额，￥1000
# donation_tax_free_salary: 捐赠个税减免
# tax: 个税
# taxed_salary: 每月税后收入
# 公积金基数上线:


class Calculator(object):
    def __init__(self, registered_house_rent, housing_fund_needed=True, unemployment_insurance_needed=True,
                 pension_needed=True, medical_insurance_needed=True):
        self.housing_fund = Insurance(HOUSING_FUND_RATE, MIN_BASE_HOUSING_FUND, MAX_BASE_HOUSING_FUND, BASE_FEE_DEFAULT)
        self.unemployment_insurance = Insurance(UNEMPLOYMENT_INSURANCE_RATE, MIN_BASE_UNEMPLOYMENT_INSURANCE_AND_PENSION, MAX_BASE_UNEMPLOYMENT_INSURANCE_AND_PENSION, BASE_FEE_DEFAULT)
        self.pension = Insurance(PENSION_RATE, MIN_BASE_UNEMPLOYMENT_INSURANCE_AND_PENSION, MAX_BASE_UNEMPLOYMENT_INSURANCE_AND_PENSION, BASE_FEE_DEFAULT)
        self.medical_insurance = Insurance(MEDICAL_INSURANCE_RATE, MIN_BASE_MEDICAL_INSURANCE, MAX_BASE_MEDICAL_INSURANCE, BASE_FEE_MEDICAL)
        self.house_rent_allowance = Allowance(tax_free_house_rent_allowance, annual_tax_free_house_rent_allowance)

        self.housing_fund_needed = housing_fund_needed
        self.unemployment_insurance_needed = unemployment_insurance_needed
        self.pension_needed = pension_needed
        self.medical_insurance_needed = medical_insurance_needed

    '''
    calculate_tax_sum 计算税费总数
    '''
    def calculate_tax_sum(self, registered_insurance_base_list, raw_salary_list, extra_tax_free_salary):
        if len(registered_insurance_base_list) != len(raw_salary_list):
            return 0
        before_tax_income_sum = sum(raw_salary_list)
        before_tax_income_sum -= sum(extra_tax_free_salary)
        before_tax_income_sum -= sum([base_tax_free_salary] * len(raw_salary_list))
        if self.pension_needed:
            before_tax_income_sum -= sum([self.pension.get_fee(x) for x in registered_insurance_base_list])
        if self.unemployment_insurance_needed:
            before_tax_income_sum -= sum([self.unemployment_insurance.get_fee(x) for x in registered_insurance_base_list])
        if self.medical_insurance_needed:
            before_tax_income_sum -= sum([self.medical_insurance.get_fee(x) for x in registered_insurance_base_list])
        if self.housing_fund_needed:
            before_tax_income_sum -= sum([self.housing_fund.get_fee(x) for x in registered_insurance_base_list])
        before_tax_income_sum -= sum([self.house_rent_allowance.get_fee(x+1) for x in range(len(raw_salary_list))])

        # 查dict，找出税率和速算扣除数
        rate, reduce_num = find_tax_range(before_tax_income_sum)
        tax_sum = before_tax_income_sum * rate - reduce_num
        return tax_sum

    '''
    calculate_every_month_salary: 给定税前收入列表，输出每月税后收入和个税
    '''
    def calculate_every_month_salary(self, registered_insurance_base_list, raw_salary_list, extra_tax_free_salary):
        if len(registered_insurance_base_list) != len(raw_salary_list) or len(raw_salary_list) != len(extra_tax_free_salary):
            return
        cur_tax_sum = 0
        for i in range(len(raw_salary_list)):
            tax_sum = self.calculate_tax_sum(registered_insurance_base_list[:i+1], raw_salary_list[:i+1], extra_tax_free_salary[:i+1])
            yield tax_sum - cur_tax_sum
            cur_tax_sum = tax_sum

    def print_tax_curve(self, registered_insurance_base_list, raw_salary_list, extra_tax_free_salary):
        for tax in self.calculate_every_month_salary(registered_insurance_base_list, raw_salary_list, extra_tax_free_salary):
            print(tax)


if __name__ == "__main__":
    c = Calculator(True)
    salary_list = [26000] * 12
    insurance_base_list = [20000] * 6 + [23967] * (len(salary_list) - 6)
    donation_tax_free_salary = [0] * 3
    donation_tax_free_salary.append(500)
    donation_tax_free_salary += [0] * (len(salary_list) - 4)
    c.print_tax_curve(insurance_base_list, salary_list, donation_tax_free_salary )
