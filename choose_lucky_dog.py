#coding=utf-8

import numpy as np
from nltk import word_tokenize

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

lucky_dog_list = []
lucky_dog_num = 5

while len(lucky_dog_list) < lucky_dog_num:
    dog_candidate = np.random.randint(1, len(num_name_dict))
    if dog_candidate not in lucky_dog_list:
        lucky_dog_list.append(dog_candidate)


for lucky_dog in lucky_dog_list:
    print num_name_dict[lucky_dog]

question = "what the fuck?"
tokens = word_tokenize(question)
print tokens



