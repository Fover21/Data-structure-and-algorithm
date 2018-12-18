# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/17
# @File: heap_sort


def sift(li, low, higt):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= higt:  # 情况2：i已经是最后一层
        if j + 1 <= higt and li[j + 1] > li[j]:  # 右孩子存在并且大于左孩子
            j += 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break  # 情况1：j位置比tmp小
    li[i] = tmp


def heap_sort(li):
    # 1 建堆
    n = len(li)
    for low in range(n // 2 - 1, -1, -1):
        sift(li, low, n - 1)
    # 2 挨个输出， 退休-棋子-调整 重复n次或n-1次
    for high in range(n - 1, -1, -1):
        li[0], li[high] = li[high], li[0]
        sift(li, 0, high - 1)


li = [1, 5, 7, 8, 3, 6, 0]
heap_sort(li)
print(li)