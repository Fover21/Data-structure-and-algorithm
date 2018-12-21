# __author: ward
# data: 2018/12/17
import random


# 算法导论思路，以结尾为基准
# def partition(li, left, right):
#     tmp = li[right]
#     i = left - 1
#     for j in range(left, right):
#         if li[j] <= tmp:  # 归到左半部分
#             i += 1
#             li[i], li[j] = li[j], li[i]
#     li[right], li[i+1] = li[i+1], li[right]
#     return i+1

def partition(li, left, right):
    # i = random.randint(left, right)
    # li[i], li[left] = li[left], li[i]
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp

    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [1, 2, 4, 0, 2, 3, 4, 9, 5]
quick_sort(li, 0, len(li) - 1)
print(li)
