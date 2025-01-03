def find_all_indices(lst, element):
    indices = [index for index, value in enumerate(lst) if value == element]
    return indices

my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_find = 2
result = find_all_indices(my_list, element_to_find)
print(result)