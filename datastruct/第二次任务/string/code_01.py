# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_01.py
@time: 2019-04-11 13:35
"""


def naive_match(source, target):
    m = len(source)
    n = len(target)
    for i in range(m-n+1):
        if source[i:i+n] == target:
            return True
    return False
    # if target in source:
    #     return True
    # else:
    #     return False


print(naive_match('abcdefghijk', 'cdefg'))
