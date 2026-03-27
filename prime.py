def prime(num):
    c=0
    for i in range(2,num):

        if num%i==0:
            c+=1
    print(c)
    
    if c==0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

a=int(input("enter a number:"))
prime(a)


