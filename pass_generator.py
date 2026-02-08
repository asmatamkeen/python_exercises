import random
import string
print("Welcome to the Password Generator!")
no_numbers=int(input("How many numbers would you like?"))
no_letters=int(input("How many letters would you like in the password?"))
no_symbol=int(input("How many symbols would you like?"))
numbers_list=[0,1,2,3,4,5,6,7,8,9]
alphabets_list=list(string.ascii_letters)
symbols_list=list(string.punctuation)
numbers=random.sample(numbers_list,no_numbers)
number_result = "".join(map(str, numbers))
letters=random.sample(alphabets_list,no_letters)
letters_result="".join(letters)
symbols=random.sample(symbols_list,no_symbol)
symbols_result="".join(symbols)
password=number_result+letters_result+symbols_result
print(password)