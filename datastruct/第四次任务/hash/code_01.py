# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_01.py
@time: 2019-04-16 0:45
"""


class LRUCache:

    def __init__(self, capacity):
        self.dic = {}
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        value = self.dic.pop(key)
        self.dic[key] = value
        return value

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem()

        self.dic[key] = value
