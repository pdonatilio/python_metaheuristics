
from tsp_00_graph_generator import *
from tsp_02_simulated_annealing_random import *
from tsp_03_genetic_algorithm import *

# Generate the Graph Example
graph = GraphGenerator(50)
graph.generate_graph()


# Simulate annealing example
print('Simulate Annealing Example')
start = time.time()
tsp_random(graph, 1000)
print('Finished in ', time.time() - start, ' seconds')


# Genetic Algorithm example
print('\nGenetic Algorithm Example')
start = time.time()
tsp_genetic(graph, population_size=100, generations=1000, tournamen_size=1, crossover_probability=0.7, mutation_propability=0.1)
print('Finished in ', time.time() - start, ' seconds')
