# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/20
# @File: is_Primel

# 方法一

import math


def is_prime_1(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def is_prime_2(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


from itertools import count


def is_prime_3(n):
    if n <= 1:
        return False
    for i in count(2):
        if i * i > n:
            return True
        if n % i == 0:
            return False


def is_prime_4(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    import sys
    for i in a:
        res = 'is_prime_%s' % i
        print(getattr(sys.modules['__main__'], res)(19))
