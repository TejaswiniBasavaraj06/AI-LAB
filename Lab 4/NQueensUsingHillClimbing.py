import random
N = int(input("Enter the number of queens: "))
def heuristic(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1
    return conflicts

def hill_climbing():
    while True:
        state = [random.randint(0, N - 1) for _ in range(N)]
        while True:
            current_h = heuristic(state)     
            if current_h == 0:
                return state
            best_state = None
            best_h = current_h
            for col in range(N):
                for row in range(N):
                    if row != state[col]:
                        neighbor = state[:]
                        neighbor[col] = row
                        h = heuristic(neighbor)
                        if h < best_h:
                            best_h = h
                            best_state = neighbor
            if best_state is None:
                break
            state = best_state

def print_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

if N < 1:
    print("Enter a positive number.")
else:
    solution = hill_climbing()
    print("Chessboard:")
    print_board(solution)