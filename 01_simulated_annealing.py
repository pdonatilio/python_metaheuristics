# OneMax problem with Simulated Annealing

import random
import math


class OneMax():

    def __init__(self, size):
        self.size = size
        self.solution = [random.randint(0, 1) for i in range(size)]
        self.cost = self.obj_fun(self.solution)

    # generate a neighbor
    def neighbor(self):
        new_neighbor = self.solution[:]
        pos = random.randint(0, self.size - 1)
        new_neighbor[pos] = 1 if new_neighbor[pos] == 0 else 0
        return new_neighbor

    # objective function
    def obj_fun(self, solution):
        return sum(solution)

    '''
        def run_anneal
        Simulated Annealing
        T        -> Initial temperature
        T_min    -> Minimum temperature
        alpha    -> Temperature decay
        max_iter -> Number of interactions with the same temperature
    '''

    def run_anneal(self, T=1.0, T_min=0.00001, alpha=0.9, max_iter=100):

        while T > T_min:

            # iteractions with the same temperature
            for i in range(max_iter):

                new_solution = self.neighbor()
                new_cost = self.obj_fun(new_solution)
                delta = self.cost - new_cost
                ap = math.exp(-delta / T)  # Acceptance probability of a worse solution

                if ap > random.random():
                    self.solution = new_solution[:]
                    self.cost = new_cost

            T = T * alpha

    def get_solution(self):
        return self.solution


one_max = OneMax(10)
print('Inicital Soluction: %s' % str(one_max.get_solution()))
one_max.run_anneal()
print('Final Soluction: %s' % str(one_max.get_solution()))
