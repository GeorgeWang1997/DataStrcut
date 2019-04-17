# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_06.py
@time: 2019-04-08 15:39
"""
import math


class Solution:
    def middleNode(self, head):

        count = 0
        res = {}
        while head != None:
            count += 1
            res[count] = head
            head = head.next

        j = math.ceil((count - 1) / 2) + 1
        return res[j]
