from create_list import random_list, is_sorted
import datetime


def merge_sort(my_list):
    """
    Perform merge sort on my_list.
    """
    def __merge(left, right):
        l, r = 0, 0
        for i in range(len(my_list)):
            left_value = left[l] if l < len(left) else None
            right_value = right[r] if r < len(right) else None

            if (not left_value == None and not right_value == None and left_value < right_value) or (not right_value and not right_value == 0):
                try:
                    my_list[i] = left_value
                except Exception as e:
                    raise e
                l += 1
            elif (not left_value == None and not right_value == None and left_value >= right_value) or (not left_value and not left_value == 0):
                my_list[i] = right_value
                r += 1
            else:
                raise Exception

    if len(my_list) <= 1:
        return

    left = my_list[0:(len(my_list) / 2)]
    right = my_list[(len(my_list) / 2):]
    merge_sort(left)
    merge_sort(right)

    __merge(left, right)

    return my_list


# my_list = [15, 73, 57, 15, 43, 94, 13, 11, 34, 87, 100, 82, 0]
my_list = random_list(14)
print(my_list)
print(is_sorted(my_list))

sorted_list = merge_sort(my_list)
print(sorted_list)
print(is_sorted(sorted_list))
