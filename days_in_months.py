def months_30():
    return "The month has 30 days"

def months_31():
    return "The month has 31 days"

def feb_month(year):
    if (year%4==0 and year % 100 !=0) or (year % 400 ==0):
        return "The month has 29 days"
    
    else:
        return "The month has 28 days"
    

month=int(input("Enter the month(1-12):"))
year=int(input("Enter the year:"))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(months_31())

elif month in [4,6,9,11]: 
    print(months_30())

elif month == 2:
    print(feb_month(year))

else:
    print("Invalid inputs")


