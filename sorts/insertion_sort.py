from create_list import random_list, is_sorted


def insertion_sort(my_list):
    """
    Perform insertion sort on my_list
    """
    for i in range(len(my_list)):
        for j in reversed(range(1, i + 1)):
            if my_list[j] < my_list[j - 1]:
                tmp = my_list[j]
                my_list[j] = my_list[j - 1]
                my_list[j - 1] = tmp
    return my_list

my_list = random_list(50)
print(my_list)
print(is_sorted(my_list))

sorted_list = insertion_sort(my_list)
print(sorted_list)
print(is_sorted(sorted_list))
