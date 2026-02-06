numbers=input("Enter numbers")
list1=numbers.split()
count=0
for num in list1:
    count=count+1
for i in range(count):
    list1[i]=int(list1[i])
print(list1)
maxi=list1[0]
for i in list1:
    if i>maxi:
        maxi=i
print(maxi)