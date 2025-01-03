def filter_numbers(lst):
    return [num for num in lst if num % 2 == 0]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = filter_numbers(nums)
print(even_nums)