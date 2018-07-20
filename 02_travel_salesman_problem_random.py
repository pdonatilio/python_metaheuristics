# Travel Salesman Problem in Python
# Solved with random method - Hamiltonian Cycle

from complete_graph import *

def tsp_random(generator,loop):

    best_circuit = []
    best_cost = None

    def create_path(best_circuit,best_cost):

        edges = [i for i in range(1, generator.n)]
        circuit = [0]
        circuit_cost = 0

        while len(edges) > 0:
            e = random.choice(edges)
            edges.remove(e)
            circuit_cost += generator.cost[(circuit[-1], e)]
            circuit.append(e)

        circuit_cost += generator.cost[(circuit[-1], 0)]

        if best_cost is None:
            best_circuit = circuit[:]
            best_cost = circuit_cost
            print('Iter %d: Best circuit: %s - Cost %d' % (i+1,str(best_circuit), best_cost))
        elif circuit_cost < best_cost:
            best_circuit = circuit[:]
            best_cost = circuit_cost

        return(best_circuit,best_cost)

    for i in range(loop):
        best_circuit,best_cost = create_path(best_circuit,best_cost)
    
        #time.sleep(1)
    print('Iter %d: Best circuit: %s - Cost %d' % (i+1,str(best_circuit), best_cost))

generator = GraphGenerator(5)
generator.generate_graph()
#generator.show_graph()
start = time.time()
tsp_random(generator,200000)
print('Finished in ',time.time()-start,' seconds')
    