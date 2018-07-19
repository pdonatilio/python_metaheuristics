#Graph generator with python

class GraphGenerator(object):
    
    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.generate_graph()

    def generate_graph(self):
        for i in range(self.n):
            #include an edge to all nodes
            for j in range(self.n):
                if i != j:
                    self.graph[i].append(j)

    def show_graph(self):
        for i in range(self.n):
            print('Nodes of %d: ' % i, end=' ')
            for node in self.graph[i]:
                print('%d' % node, end=' -> ')
            print()




generator = GraphGenerator(10)
#generator.generate_graph()
generator.show_graph()