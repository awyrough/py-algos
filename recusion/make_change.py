import time

def make_optimal_change(coins, change, known_results=None):
    """
    Using coins in coins, make change for change.
    """
    min_coins = change
    if min_coins in coins:
        if known_results:
            known_results[min_coins] = 1
        return 1
    elif known_results and known_results[min_coins] > 0:
        return known_results[min_coins]

    for i in [coin for coin in coins if coin < change]:
        num_coins = 1 + make_optimal_change(coins, change - i, known_results=known_results)
        min_coins = min(num_coins, min_coins)
        if min_coins == num_coins and known_results:
            known_results[change] = min_coins

    return min_coins

start_time = time.clock()
print start_time

change = make_optimal_change([1, 5, 10, 25], 63, known_results=None)
print change

start_time = time.clock()
print start_time

change = make_optimal_change([1, 5, 10, 25], 63, known_results=[0 for x in range(64)])
print change

start_time = time.clock()
print start_time
