def count(input_string):
    vowels = "aeiouAEIOU"
    consonants = 0
    vowels_count = 0

    for char in input_string:
        if char.isalpha():  
            if char in vowels:
                vowels_count += 1
            else:
                consonants += 1

    return vowels_count, consonants

input_str = str(input())
vowels, consonants = count(input_str)
print(f"Vowels: {vowels}, Consonants: {consonants}")

# O'zim yozmadim lekin 