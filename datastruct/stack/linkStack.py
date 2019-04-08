# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: linkStack.py
@time: 2019-04-06 21:11
"""


class Node:

    def __init__(self, value=0, nex=None):
        self.value = value
        self.nex = nex

    def __str__(self):
        return str(self.value)


class LinkStack:

    def __init__(self, length):
        self.stack = Node()
        self.length = length
        self.max = 0

    def push(self, value):
        if self.stack.value is None:
            self.stack.value = value
        elif self.max < self.length:
            node = Node(value=value, nex=self.stack)
            self.stack = node
            print(self.stack)
            self.max += 1
        else:
            print("栈已满")

    def pop(self):
        if self.max > 0:
            self.stack = self.stack.nex
            self.max -= 1
        else:
            print("栈已空")

    def peek(self):
        return self.stack.value

    def is_empty(self):
        if self.stack.value is None:
            return True
        return False


if __name__ == '__main__':
    linkStack = LinkStack(3)
    for i in range(4):
        linkStack.push(i)
    print(linkStack.max)
    for i in range(4):
        linkStack.pop()
    print(linkStack.max)
