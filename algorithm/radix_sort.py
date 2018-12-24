# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/24
# @File: radix_sort

##############################################
# def get_digit(num, i):  # 获取整数第i位数字  #
#     return num // (10 ** i) % 10           #
#                                            #
#                                            #
# def int_to_list(num):                      #
#     li = []                                #
#     while num > 0:                         #
#         li.append(num % 10)                #
#         num = num // 10                    #
#     li.reverse()                           #
#     return li                              #
##############################################


def list_to_buckets(li, i):
    buckets = [[] for _ in range(10)]
    for num in li:
        digit = num // (10 ** i) % 10
        buckets[digit].append(num)
    return buckets


def buckets_to_list(buckets):
    li = []
    for bucket in buckets:
        for num in bucket:
            li.append(num)
    return li
    # return [num for bucket in buckets for num in bucket]


def radix_sort(li):
    max_val = max(li)
    i = 0
    while 10 ** i <= max_val:
        li = buckets_to_list(list_to_buckets(li, i))
        i += 1
    return li


print(radix_sort([5, 3, 9, 8, 1, 0, 99]))
