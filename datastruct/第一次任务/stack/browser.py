# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: browser.py
@time: 2019-04-06 22:02
"""


class Browser:

    def __init__(self):
        self.next = []
        self.previous = []

    def advance(self):
        if len(self.next) > 0:
            self.next.pop()
            self.previous.append('<')
        else:
            print('无法前进')
            return
        print(''.join(self.previous), '  ', ''.join(self.next))

    def back(self):
        if len(self.previous) > 0:
            self.previous.pop()
            self.next.append('>')
        else:
            print('无法后退')
            return
        print(''.join(self.previous), '  ', ''.join(self.next))

    def new(self):
        self.previous.append('<')
        self.next.clear()
        print(''.join(self.previous), '  ', ''.join(self.next))


if __name__ == '__main__':
    browser = Browser()
    browser.next = ['>', '>']
    browser.previous = ['<', '<']
    print("1后退，2前进，3新页面")
    while True:
        choice = int(input())
        if choice == 1:
            browser.back()
        elif choice == 2:
            browser.advance()
        elif choice == 3:
            browser.new()
