heights=input("Enter heights:")
height_list=heights.split()
print(height_list)
count=0
total=0
for counts in height_list:
    count=count+1
for i in range(count):
    height_list[i]=int(height_list[i])
for height in height_list:
    total=total+height
avg=total/count
print(f"length of height list is {count}")
print(f"Average of heights is {avg}")