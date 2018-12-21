# __author: ward
# data: 2018/12/17


def bin_search(li, num):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == num:
            return mid
        elif li[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


li = [1, 2, 5, 6, 7, 8, 10]
print(bin_search(li, 7))

from bisect import *


def bisectSearch(lst, x):
    i = bisect_left(lst, x)  # bisect_left(lst,x)，得到x在已经排序的lst中的位置
    if i != len(lst) and lst[i] == x:
        return i
    raise ValueError

print(bisectSearch(li, 7))
