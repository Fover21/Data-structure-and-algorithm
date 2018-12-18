# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/17
# @File: merge_sort


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    # li[low:high+1] = li_tmp
    for k in range(low, high + 1):
        li[k] = li_tmp[k - low]


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


li = [1, 0, 5, 7, 3, 8, 3, 5, 4]
merge_sort(li, 0, len(li) - 1)
print(li)
