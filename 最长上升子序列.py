# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/18
# @File: 最长上升子序列


def long_increasing_sequence(nums):
    dp = [1 for i in range(len(nums))]
    max_result = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if (nums[j] < nums[i]):
                dp[i] = max(dp[i], dp[j] + 1)
        max_result = max(dp[i], max_result)
    return max_result


print(long_increasing_sequence([5, 4, 1, 2, 3, 4]))
