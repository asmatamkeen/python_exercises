total=0
num=int(input(("enter a num:(9 for exit)")))
while num!=9:
    total=total+num
    num=int(input(("enter a num:(9 for exit)")))
else:
    print("in else block")
print(f"total={total}")