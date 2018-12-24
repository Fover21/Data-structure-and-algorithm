# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/24
# @File: shell_sort

import random


def insert_sort_gap(li, d):
    for i in range(d, len(li)):
        j = i - d
        temp = li[i]
        while j >= 0 and li[j] > temp:
            li[j + d] = li[i]
            j -= d
        li[j + d] = temp


def shell_sort(li):
    d = len(li) // 2
    while d > 0:
        insert_sort_gap(li, d)
        d = d // 2


li = list(range(10))
random.shuffle(li)
shell_sort(li)
print(li)