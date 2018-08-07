# Travel Salesman Problem in Python
# Solved with Simulated Annealing (random method - Hamiltonian Cycle)

from tsp_00_graph_generator import *


def tsp_random(graph, loop):

    best_circuit = []
    best_score = None

    def create_circuit(best_circuit, best_score):

        edges = [i for i in range(1, graph.n)]
        circuit = [0]
        circuit_score = 0

        while len(edges) > 0:
            e = random.choice(edges)
            edges.remove(e)
            circuit_score += graph.score[(circuit[-1], e)]
            circuit.append(e)

        circuit_score += graph.score[(circuit[-1], 0)]

        if best_score is None:
            best_circuit = circuit[:]
            best_score = circuit_score
            print('Iter %d: Best circuit: %s - score %d' % (i + 1, str(best_circuit), best_score))
        elif circuit_score < best_score:
            best_circuit = circuit[:]
            best_score = circuit_score

        return(best_circuit, best_score)

    for i in range(loop):
        best_circuit, best_score = create_circuit(best_circuit, best_score)

        # time.sleep(1)
    print('Iter %d: Best circuit: %s - score %d' % (i + 1, str(best_circuit), best_score))
