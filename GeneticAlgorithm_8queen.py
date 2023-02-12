import random

def fitness_fn(individual):
    fitness = 28
    for i in range(7):
        for j in range(i + 1, 8):
            if abs(individual[i] - individual[j]) == abs(i - j) or individual[i] == individual[j]:
                fitness -= 1
                break
    return fitness


def select_parents(population, fitness_fn, num_parents):
    population = sorted(population, key=lambda x: fitness_fn(x), reverse=True)
    return population[:num_parents]

def crossover(parents, offspring_size):
    offspring = []
    for i in range(offspring_size):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        offspring.append(parent1[:4] + parent2[4:])
    return offspring

def mutation(offspring):
    for k in range(len(offspring)):
        for i in range(7):
            for j in range(i + 1, 8):
                if abs(offspring[k][i] - offspring[k][j]) == abs(i - j) or offspring[k][i] == offspring[k][j]:
                    offspring[k][j] = random.randint(1, 9)
    return offspring

def genetic_algorithm(population, fitness_fn, pop_size, num_parents):
    i = 1
    while True:
        parents = select_parents(population, fitness_fn, num_parents)
        offspring = crossover(parents, pop_size - num_parents)
        offspring = mutation(offspring)
        population = parents + offspring
        print("Generation", i, "best fitness =", fitness_fn(parents[0]) )
        if fitness_fn(parents[0]) == 28:
            break
        i = i + 1
    return parents[0]

population = [[random.choice(range(1,9)) for _ in range(8) ] for _ in range(10)]
result = genetic_algorithm(population, fitness_fn, 10, 6)
print("Result: ", result)
