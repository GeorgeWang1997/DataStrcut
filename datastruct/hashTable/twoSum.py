# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: twoSum.py
@time: 2019-04-11 13:31
"""


def two_sum(nums, target):
    dic = {}
    for i in range(len(nums)):
        y = target - nums[i]
        if nums[i] in dic:
            return dic[nums[i]], i
        else:
            dic[y] = i

    for i, x in enumerate(nums):
        y = target - x
        if y in nums[i+1:]:
            return [i, nums[i+1:].index(y)+i+1]
