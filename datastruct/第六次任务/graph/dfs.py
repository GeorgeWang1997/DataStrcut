# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: dfs.py
@time: 2019-04-21 23:58
"""


class Graph:

    def __init__(self):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if u != v:
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    # 深度优先
    def depth_first_search(self, root=None):
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if n not in self.visited:
                    dfs(n)

        if root:
            dfs(root)

        for node in self.nodes():
            if node not in self.visited:
                dfs(node)

        print(order)
        return order

    # 广度优先
    def breadth_first_search(self, root=None):
        queue = []
        order = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)

                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (n not in self.visited) and (n not in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if node not in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        print(order)

        return order
