# Graph generator with python

import random
import time


class GraphGenerator(object):

    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.cost = {}

    def generate_graph(self):

        for i in range(self.n):
            # include an edge to all nodes
            for j in range(self.n):
                if i != j:
                    if ((i, j) and (j, i)) not in self.cost:
                        cost = random.randint(1, 100)
                        self.cost[(i, j)] = cost
                        self.cost[(j, i)] = cost

                    self.graph[i].append(j)

    def show_graph(self):
        for i in range(self.n):
            print('Nodes connecteds to %d: ' % i, end=' ')
            for node in self.graph[i]:
                print('[%d to %d the cost is %d]' % (i, node, self.cost[i, node]), end='\t ')
            print()

    