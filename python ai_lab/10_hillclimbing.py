import random

# Objective function
def f(x):
    return -x**2 + 5*x


def hill_climbing(start):

    current = start

    while True:

        neighbor1 = current + 1
        neighbor2 = current - 1

        best = current

        if f(neighbor1) > f(best):
            best = neighbor1

        if f(neighbor2) > f(best):
            best = neighbor2

        if best == current:
            return current

        current = best


start = random.randint(-10,10)

solution = hill_climbing(start)

print("Start:", start)
print("Best solution:", solution)
print("Maximum value:", f(solution))