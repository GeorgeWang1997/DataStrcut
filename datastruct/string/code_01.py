# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_01.py
@time: 2019-04-11 13:35
"""


def naive_match(s, p):
    m = len(s)
    n = len(p)
    for i in range(m-n+1):
        if s[i:i+n] == p:
            return True
    return False
