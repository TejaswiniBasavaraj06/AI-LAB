import math
import random

def initial_state(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]

def calculate_cost(state):
    n = len(state)
    attacking_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def get_random_neighbour(state):
    neighbour = list(state)
    col = random.randint(0, len(state) - 1)
    new_row = random.randint(0, len(state) - 1)
   
    while new_row == state[col]:
        new_row = random.randint(0, len(state) - 1)
       
    neighbour[col] = new_row
    return neighbour

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

def simulated_annealing(n=8, initial_temp=1000.0, cooling_rate=0.99, min_temp=0.00001):
    current = initial_state(n)
    T = initial_temp
    steps = 0
   
    while T > min_temp:
        current_cost = calculate_cost(current)
        if current_cost == 0:
            print(f"Solution found in {steps} iterations!")
            return current
       
        next_state = get_random_neighbour(current)
        next_cost = calculate_cost(next_state)
        delta_E = current_cost - next_cost
       
        if delta_E > 0:
            current = next_state
        else:
            p = math.exp(delta_E / T)
            if random.random() < p:
                current = next_state
       
        T *= cooling_rate
        steps += 1
       
    return current


if __name__ == "__main__":
    print("=== Simulated Annealing: 8-Queens Problem ===\n")
   
    solution = simulated_annealing(n=8)
    final_cost = calculate_cost(solution)
   
    print(f"Final State Representation (column -> row): {solution}")
    print(f"Final Cost (Attacking Pairs): {final_cost}\n")
   
    print("Board Visualisation:")
    print_board(solution)