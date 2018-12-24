# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/24
# @File: count_sort

import random


def count_sort(li, max_num=100):
    count = [0 for i in range(max_num + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for i in range(len(count)):
        # i这个数出现了count[i]次
        # li.extend([i]*count[i])
        for _ in range(count[i]):
            li.append(i)


li = [random.randint(0, 100) for _ in range(20)]
count_sort(li)
print(li)
