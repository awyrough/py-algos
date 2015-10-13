import random

random_list = lambda x: [random.randint(0, 100) for i in range(x)]


def is_sorted(x):
    for i in range(1, len(x) - 1):
        if not (x[i - 1] <= x[i] <= x[i + 1]):
            return False
    return True
