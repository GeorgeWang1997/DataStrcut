# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: slideWindow.py
@time: 2019-04-13 16:18
"""


def slide_window(nums, k):
    if not nums:
        return []
    window, res = [], []
    for i, x in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and nums[window[-1]] <= x:
            window.pop()
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res
