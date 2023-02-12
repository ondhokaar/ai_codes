import random

def random_restart_hill_climbing(fitness_fn, max_restarts=100):
    best_x, best_fitness = None, float('-inf')
    
    for i in range(max_restarts):
        current_x = random.uniform(1, 100)
        current_fitness = fitness_fn(current_x)
        
        for j in range(100):
            neighbors = [current_x + random.uniform(0, 1) for _ in range(5)]
                
            next_x = random.choice(neighbors)
            next_fitness = fitness_fn(next_x)
            
            if next_fitness > current_fitness:
                current_x, current_fitness = next_x, next_fitness
                
                if current_fitness > best_fitness:
                    best_x, best_fitness = current_x, current_fitness
                    
            else:
                break
                
    return best_x

def fitness_fn(x):
    return x**2

best_x = random_restart_hill_climbing(fitness_fn)

print("Best state:", best_x)
print("Fitness:", fitness_fn(best_x))
