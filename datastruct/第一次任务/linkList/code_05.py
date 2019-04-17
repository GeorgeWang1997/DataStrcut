# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_05.py
@time: 2019-04-08 15:38
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            ret = l1
            ret.next = self.mergeTwoLists(l1.next, l2)
        else:
            ret = l2
            ret.next = self.mergeTwoLists(l1, l2.next)
        return ret