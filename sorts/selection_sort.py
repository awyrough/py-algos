from create_list import random_list, is_sorted


def selection_sort(my_list):
    """
    Perform selection sort on my_list
    """
    for i, k in enumerate(my_list):
        for j, l in enumerate(my_list[i+1:]):
            if l < k:
                k = l
                swap = j + i + 1
        if k != my_list[i]:
            my_list[i], my_list[swap] = my_list[swap], my_list[i]
    return my_list

my_list = random_list(50)
print(my_list)
print(is_sorted(my_list))

sorted_list = selection_sort(my_list)
print(sorted_list)
print(is_sorted(sorted_list))
