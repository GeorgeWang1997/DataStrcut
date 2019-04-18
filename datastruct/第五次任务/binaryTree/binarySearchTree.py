# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: binarySearchTree.py
@time: 2019-04-18 12:44
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, val=None):
        if val:
            self.root = Node(val)
        else:
            self.root = None

    # 插入
    def insert(self, root, val):
        if root is None:
            root = Node(val)
        elif root.val >= val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    # 查找
    def query(self, root, val):
        if root is None:
            return False
        if root.val == val:
            return root
        elif root.val > val:
            self.query(root.left, val)
        else:
            self.query(root.right, val)

    # 查找最小值
    def find_min(self, root):
        if root.left:
            return self.find_min(root.left)
        else:
            return root

    # 查找最大值
    def find_max(self, root):
        if root.right:
            return self.find_max(root.right)
        else:
            return root

    # 查找前驱
    def precursor(self, root, val):
        node = self.query(root, val)
        if node:
            while root:
                if root.left.val == val or root.right.val == val:
                    return root
                elif val < root.left.val:
                    root = root.left
                else:
                    root = root.right

    # 查找后继
    def succeed(self, root, val):
        root = self.query(root, val)
        return [root.left, root.right]

    # 删除节点
    def delete(self, root, val):
        if root is None:
            return
        if root.val > val:
            self.delete(root.left, val)
        elif root.val < val:
            self.delete(root.right, val)
        else:
            if root.left and root.right:
                temp = self.find_min(root.right)
                root.val = temp.val
                self.delete(root.right, temp.val)
            elif root.left is None and root.right is None:
                root = None
            elif root.right is None:
                root = root.left
            elif root.left is None:
                root = root.right
        return root

    # 前序遍历
    def pre_order(self, root):
        if root is None:
            return
        print(root.val, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    # 中序遍历
    def in_order(self, root):
        if root is None:
            return
        self.pre_order(root.left)
        print(root.val, end=' ')
        self.pre_order(root.right)

    # 后序遍历
    def post_order(self, root):
        if root is None:
            return
        self.pre_order(root.left)
        self.pre_order(root.right)
        print(root.val, end=' ')

    # 层序遍历
    def lever_order(self, root):
        if root is None:
            return
        queue = []
        res = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return res
