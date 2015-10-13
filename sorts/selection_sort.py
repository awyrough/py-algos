from create_list import random_list, is_sorted


def selection_sort(my_list):
    """
    Perform selection sort on my_list
    """
    for i in range(len(my_list)):
        new_min = my_list[i]
        for j in range(i + 1, len(my_list)):
            if my_list[j] < new_min:
                new_min = my_list[j]
                swap = j

        if new_min != my_list[i]:
            tmp = my_list[i]
            my_list[i] = new_min
            my_list[swap] = tmp
    return my_list

my_list = random_list(50)
print(my_list)
print(is_sorted(my_list))

sorted_list = selection_sort(my_list)
print(sorted_list)
print(is_sorted(sorted_list))
