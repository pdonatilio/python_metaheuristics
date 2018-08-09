# Knapsack Problem Using Tabu Search in Python

import random

knapsack = [[4, 2], [5, 2], [7, 3], [9, 4], [6, 4]]  # knapsack configuration [weight, value]
move, best_move = 0, 0
best_solution = []
tabu_list = []
capacity = 23  # Knapsack maximum capacity
bt_max = 1  # maximum of movements allowed without the solution improvement
max_neighborhood = 5  # maximum of neighbors allowed

# Get the solution value


def get_value(solution, knapsack, capacity):
    sum_weight, sum_value = 0, 0

    for i in range(len(solution)):
        sum_weight += solution[i] * knapsack[i][0]
        sum_value += solution[i] * knapsack[i][1]

    value = sum_value * (1 - max(0, sum_weight - capacity))

    return value

# Get the solution weight


def get_weight(solution, knapsack):
    weight = 0
    for i in range(len(solution)):
        weight += solution[i] * knapsack[i][0]

    return weight

# Generate the Neighborhood


def neighborhood_generate(best_solution, max_neighborhood):
    neighbors, pos = [], 0

    for i in range(max_neighborhood):
        neighbor = []
        for j in range(len(best_solution)):
            if j == pos:
                if best_solution[j] == 0:
                    neighbor.append(1)
                else:
                    neighbor.append(0)
            else:
                neighbor.append(best_solution[j])
        neighbors.append(neighbor)
        pos += 1

    return neighbors

# get neighborhood values list


def get_neighbors_values(neighbors, knapsack, capacity, max_neighborhood):
    neighbors_values = []

    for i in range(max_neighborhood):
        neighbors_values.append(get_value(neighbors[i], knapsack, capacity))

    return neighbors_values

# Get the changed bit


def get_bit(best_solution, best_neighbor):
    for i in range(len(best_solution)):
        if best_solution != best_neighbor[i]:
            return i

# Get the most evaluated neighbor


def get_most_evaluated_neighbor(neighbors_values, tabu_list, best_solution, neighbors):
    max_value = max(neighbors_values)
    pos = 0
    forbidden_bit = -1

    # The Tabu list is not empty?
    if len(tabu_list) != 0:
        # if have something, we have a forbidden bit, we need to get this
        forbidden_bit = tabu_list[0]

    # Get the best neighbor position
    for i in range(len(neighbors_values)):
        if neighbors_values[i] == max_value:
            pos = i
            break

    # get if this neighbor have a forbidden bit
    if forbidden_bit != -1:
        # get the bit changed position
        bit_pos = get_bit(best_solution, neighbors[pos])

        # check if the bit is inside of the tabu list
        if bit_pos == forbidden_bit:

            # we need looking for the second best neighbor
            best_pos = 0

            for i in range(len(neighbors_values)):
                if i != bit_pos:
                    if neighbors_values[i] > neighbors_values[best_pos]:
                        best_pos = i

            return best_pos  # return second best neighbor position

    return pos  # return the best neighbor position

# Generate a random solution
for x in range(len(knapsack)):
    bit = random.randint(0, 1)
    best_solution.append(bit)

print('Initial Solution: {0}, Value: {1}'.format(best_solution, get_value(best_solution, knapsack, capacity)))

# get the knapsack current weight
current_weight = get_weight(best_solution, knapsack)

# get te best solution value
best_value = get_value(best_solution, knapsack, capacity)

# generate neighborhood
neighborhood = neighborhood_generate(best_solution, max_neighborhood)

# get the neighbors values
neighbors_values = get_neighbors_values(neighborhood, knapsack, capacity, max_neighborhood)

# get the best neighbor position
best_neighbor_position = get_most_evaluated_neighbor(neighbors_values, tabu_list, best_solution, neighborhood)

# check if the best neighbor have value better than the best solution
if neighbors_values[best_neighbor_position] > best_value:

    # get the neighbor's changed bit
    changed_bit = get_bit(best_solution, neighborhood[best_neighbor_position])

    # keep the forbidden bit
    tabu_list.append(changed_bit)

    # get a copy of the this solution
    best_solution = neighborhood[best_neighbor_position][:]

    # update the best moviment
    best_move += 1

move += 1

while True:

    # When (move - best_move) > bt_max is time to stop this loop
    #print('Move: {0}, The best move: {1}, the bt_max: {2}, (move - best_move) > bt_max: {3}'.format(move,best_move,bt_max, (move - best_move) > bt_max))
    if (move - best_move) > bt_max:
        break

    # generate a new neighborhood
    neighborhood = neighborhood_generate(best_solution, max_neighborhood)

    # get the neighbors values
    neighbors_values = get_neighbors_values(neighborhood, knapsack, capacity, max_neighborhood)[:]

    # get the best neighbor position
    best_neighbor_position = get_most_evaluated_neighbor(neighbors_values, tabu_list, best_solution, neighborhood)

    # check if the best neighbor have value better than the best solution
    if neighbors_values[best_neighbor_position] > best_value:

        # get the neighbor's changed bit
        changed_bit = get_bit(best_solution, neighborhood[best_neighbor_position])

        # keep the forbidden bit
        tabu_list[0] = changed_bit

        # get a copy of the this solution
        best_solution = neighborhood[best_neighbor_position][:]

        best_value = neighbors_values[best_neighbor_position]

        # update the best moviment
        best_move += 1

    move += 1

# Get the final solution and your value
print('Final Solution: {0}, Value: {1}'.format(best_solution,get_value(best_solution, knapsack, capacity)))
print('Best Movement: {0}'.format(best_move))
print('Movement: {0}'.format(move))