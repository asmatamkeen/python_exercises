if __name__ == '__main__':
    n = int(input("enter n:"))
    arr = map(int, input("Enter scores:").split())

list1 = set(list(arr))
maxi=max(list1)
list1.remove(maxi)
print(max(list1))