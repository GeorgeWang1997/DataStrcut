# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: arrayStack.py
@time: 2019-04-06 20:13
"""


class ArrayStack:

    def __init__(self, length):
        self.stack = []
        self.length = length

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, element):
        if len(self.stack) == self.length:
            print("栈已满")
        else:
            self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("栈已空")

    def show(self):
        print(self.stack)

    def clear(self):
        self.stack.clear()

    def peek(self):
        return self.stack[len(self.stack)-1]


if __name__ == '__main__':
    arrayStack = ArrayStack(3)
    for i in range(4):
        arrayStack.push(i)
    arrayStack.show()
    print("栈顶元素：", arrayStack.peek())
    print(arrayStack.is_empty())
    for i in range(4):
        arrayStack.pop()
    print(arrayStack.is_empty())
