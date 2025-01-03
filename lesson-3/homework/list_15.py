numbers=list(input('enter list:'))
def count_even_numbers(numbers):
   count = 0
   for num in numbers:
    if num % 2 == 0:
     count += 1
   return count

print(count_even_numbers(numbers)) 










