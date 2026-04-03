import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def op_input():
    print("+\n-\n*\n/")
    op=input("Pick an operator:")
    return op

def operation(f_num,op,s_num):
    if op == '+':
        result=f_num + s_num
        print(f"{f_num} + {s_num} = {result}")
        return result

    elif op == '-':
        result=f_num - s_num
        print(f"{f_num} - {s_num} = {result}")
        return result
    
    elif op == '*':
        result=f_num * s_num
        print(f"{f_num} * {s_num} = {result}")
        return result
    
    elif op == '/':
        result=f_num / s_num
        print(f"{f_num} / {s_num} = {result}")
        return result
    
    else:
        return "Invalid input"
 
 


first_num=int(input("Enter first number:"))
operator=op_input()
second_num=int(input("Enter second number:"))
result=operation(first_num,operator,second_num)



while True:
    user_input=input(f"Enter 'y' to continue calculation with {result} or'n' to start new calculation or 'x' to exit:")
    if user_input == 'y':
        first_num=result 
        operator=op_input()
        second_num=int(input("Enter second number:"))
        result=operation(first_num,operator,second_num)

    elif user_input == 'n':
        clear_screen()
        first_num=int(input("Enter first number:"))
        operator=op_input()
        second_num=int(input("Enter second number:"))
        result=operation(first_num,operator,second_num)

    else:
        break;







