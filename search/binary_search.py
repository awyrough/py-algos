import random

random_list = lambda x: [random.randint(0, 100) for i in range(x)]


def binary_search(my_list, key):
    """
    Return true if key in list, false if not.

    List is assumed to a be a sorted list (ascending)
    """
    if len(my_list) == 0:
        return False

    low = 0
    high = len(my_list) - 1

    while low <= high:
        midpoint = (high + low) // 2
        if key == my_list[midpoint]:
            return True
        if key < my_list[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1
    else:
        return False


my_list = random_list(random.randint(0, 20))
my_list = sorted(my_list)
random_key = random.randint(0, 100)

print "Did it work?"
print (binary_search(my_list, random_key) == (random_key in my_list))
