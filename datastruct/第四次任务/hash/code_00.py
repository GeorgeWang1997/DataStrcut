# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_00.py
@time: 2019-04-16 0:45
"""


class _ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashMap:
    def __init__(self, size):
        self._table = [None] * size
        self._n = 0

    def __len__(self):
        return self._n

    def _hash(self, key):
        return abs(hash(key) % len(self._table))

    def __getitem__(self, key):
        j = self._hash(key)
        node = self._table[j]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            raise Exception
        return node

    def insert(self, key):
        try:
            self[key]
        except KeyError:
            j = self._hash(key)
            node = self._table[j]
            self._table[j] = _ListNode(key)
            self._table[j].next = node
            self._n += 1

    def __delitem__(self, key):
        j = self._hash(key)
        node = self._table[j]
        if node is not None:
            if node.key == key:
                self._table[j] = node.next
                self._n -= 1
            else:
                while node.next is not None:
                    pre = node
                    node = node.next
                    if node.key == key:
                        pre.next = node.next
                        self._n -= 1
                        break
