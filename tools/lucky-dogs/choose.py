#!/usr/bin/python3

"""
===============================================================================
author: 赵明星
desc:   我们一起来抓阄。
===============================================================================
"""


import numpy as np


def choose_lucky_dog(candidates, total_dog_num):
    dogs = []
    while len(dogs) < total_dog_num:
        dog_candidate = np.random.randint(1, len(num_name_dict))
        if dog_candidate not in dogs:
            dogs.append(dog_candidate)
    return [candidates[lucky_dog] for lucky_dog in dogs]


if __name__ == "__main__":
    num_name_dict = {
                1: "赵明星",
                2: "陈琨",
                3: "蒲黎明",
                4: "张庆恒",
                5: "康家鹏",
                6: "郭明",
                7: "肖宗阳",
                8: "王刘"
                }
    print(choose_lucky_dog(num_name_dict, 5))

