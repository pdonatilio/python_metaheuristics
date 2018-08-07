# Travel Salesman Problem in Python
# Solved with Genetic Algorithm

from tsp_00_graph_generator import *


def tsp_genetic(graph, population_size, generations, tournamen_size, crossover_probability, mutation_propability):

    population = []

    def create_individuals():

        edges = [i for i in range(1, graph.n)]
        individual = [0]

        while len(edges) > 0:
            e = random.choice(edges)
            edges.remove(e)
            individual.append(e)

        return(individual)

    def get_fitness_score(individual):
        score = 0
        for i in range(graph.n - 1):
            score += graph.score[(individual[i], individual[i + 1])]
        score += graph.score[(individual[-1], individual[0])]

        return score

    # Generating of initial population
    for i in range(population_size):
        population.append(create_individuals())

    # Create a new generation
    for i in range(generations):
        # Using tournament selection
        for j in range(tournamen_size):
            if random.random() <= crossover_probability:
                # Individuals to generate 2 new childrens (population size control)
                parent1, parent2 = None, None

                # This is not a better way to get new unique individuals
                # Maybe fix this in the future
                while True:
                    parent1 = random.randint(0, population_size - 1)
                    parent2 = random.randint(0, population_size - 1)
                    if parent1 != parent2:
                        break

                # New empty children
                child1, child2 = [], []

                # Valid Genes to use in Crossover
                valid_genes_parent1 = [i for i in range(graph.n)]
                valid_genes_parent2 = valid_genes_parent1[:]

                # Single Point Crossover
                while True:

                    point = random.randint(0, graph.n - 1)  # Gene Separator

                    if point != 0 and point != (graph.n - 1):  # Never use the extremities

                        for p in range(point):  # First Gene Part
                            # We can't use a same node 2 times here
                            # if occurs then use other aleatory item
                            if population[parent1][p] not in child1:
                                child1.append(population[parent1][p])
                                valid_genes_parent1.remove(population[parent1][p])
                            else:
                                gene = random.choice(valid_genes_parent1)  # chosen aleatory item
                                child1.append(gene)
                                valid_genes_parent1.remove(gene)

                            # The same to child 2
                            if population[parent2][p] not in child2:
                                child2.append(population[parent2][p])
                                valid_genes_parent2.remove(population[parent2][p])
                            else:
                                gene = random.choice(valid_genes_parent2)  # chosen aleatory item
                                child2.append(gene)
                                valid_genes_parent2.remove(gene)

                        for p in range(point, graph.n):  # Second Gene Part
                            # We can't use a same node 2 times here again
                            # if occurs then use other aleatory item
                            if population[parent2][p] not in child1:
                                child1.append(population[parent2][p])
                                valid_genes_parent1.remove(population[parent2][p])
                            else:
                                gene = random.choice(valid_genes_parent1)  # chosen aleatory item
                                child1.append(gene)
                                valid_genes_parent1.remove(gene)

                            # The same to child 2
                            if population[parent1][p] not in child2:
                                child2.append(population[parent1][p])
                                valid_genes_parent2.remove(population[parent1][p])
                            else:
                                gene = random.choice(valid_genes_parent2)  # chosen aleatory item
                                child2.append(gene)
                                valid_genes_parent2.remove(gene)

                        break

                # Applying the mutation probability operator
                if random.random() <= mutation_propability:
                    gene1, gene2 = None, None

                    while True:
                        gene1 = random.randint(0, graph.n - 1)
                        gene2 = random.randint(0, graph.n - 1)
                        if gene1 != gene2:
                            child1[gene1], child1[gene2] = child1[gene2], child1[gene1]
                            child2[gene1], child2[gene2] = child2[gene2], child2[gene1]
                            break

                # Get the fitness score
                fitness_parent1 = get_fitness_score(population[parent1])
                fitness_parent2 = get_fitness_score(population[parent2])
                fitness_child1 = get_fitness_score(child1)
                fitness_child2 = get_fitness_score(child2)

                # Find the fitness value and keeping the same size of population
                if fitness_child1 < fitness_parent1 or fitness_child1 < fitness_parent2:
                    if fitness_child1 < fitness_parent1:
                        population.pop(parent1)
                    else:
                        population.pop(parent2)
                    population.append(child1)

                elif fitness_child2 < fitness_parent1 or fitness_child2 < fitness_parent2:
                    if fitness_child2 < fitness_parent1:
                        population.pop(parent1)
                    else:
                        population.pop(parent2)
                    population.append(child2)

            # Getting the best individual score
            best_individual = population[0][:]
            for individual in range(1, population_size):
                if get_fitness_score(population[individual]) < get_fitness_score(best_individual):
                    best_individual = population[individual][:]

            if i == 0:
                print('Iteration %d:\nBest individual %s - Cost: %d' % (i + 1, str(best_individual), get_fitness_score(best_individual)))
    print('Iteration %d:\nBest individual %s - Cost: %d' % (i + 1, str(best_individual), get_fitness_score(best_individual)))
