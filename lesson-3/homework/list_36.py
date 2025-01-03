list1= [1, -2, 3, -4, 5, 6, -7]
def sum(list1):
    total = 0
    for number in list1:
        if number > 0:
            total += number
    return total

print(sum(list1))