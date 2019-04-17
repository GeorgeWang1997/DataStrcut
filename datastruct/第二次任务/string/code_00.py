# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_00.py
@time: 2019-04-11 13:35
"""


class Trie:

    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def insert(self, chars):
        node = self.root
        for char in chars:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def serach(self, chars):
        node = self.root
        for char in chars:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

