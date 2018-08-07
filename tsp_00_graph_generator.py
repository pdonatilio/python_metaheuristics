# Graph generator with python

import random
import time


class GraphGenerator():

    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.score = {}

    def generate_graph(self):

        for i in range(self.n):
            # include an edge to all nodes
            for j in range(self.n):
                if i != j:
                    if ((i, j) and (j, i)) not in self.score:
                        score = random.randint(1, 100)
                        self.score[(i, j)] = score
                        self.score[(j, i)] = score

                    self.graph[i].append(j)

    def show_graph(self):
        for i in range(self.n):
            print('Nodes connecteds to %d: ' % i, end=' ')
            for node in self.graph[i]:
                print('[%d to %d the score is %d] ' % (i, node, self.score[i, node]), end='\t ')
            print()
