def contains_digits(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False
input_string = input("Enter a string: ")
if contains_digits(input_string):
    print('True')
else:
    print('false')


    #o'zimnikimas Al dan yordam oldim 