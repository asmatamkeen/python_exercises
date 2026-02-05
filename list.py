list1=[1,1,1]
list2=[1,1,1]
list3=[1,1,1]
final_list=[list1, list2, list3]
print(final_list)
a=input("Enter the position:")
row=int(a[0])
column=int(a[1])
position=str(row-1)+str((column-1))
print(f"position selected is{position}")
print(type(row-1))

final_list[row-1][column-1]='x'
print(final_list)