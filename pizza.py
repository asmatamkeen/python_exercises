pizza=input("Size of pizza:(S for small, m for medium and l for large)")
bill=0
if pizza=='s' or pizza=='S':
    bill=100
    print("price=100")
    
elif pizza=='m' or pizza=='M':
    bill=200
    print("price=200")
else :
    bill=300
    print("price=300")
pep=input("pepperoni?(y/n)")
if pep=='y' or pep=='Y':
    if pizza=='s' or 'S':
        bill+=30
        print("price=",bill)
    else:
        bill+=50
        print("price=",bill)

cheese=input("cheese?(y/n)")
if cheese=='y' or cheese=='Y':
    bill+=20
    print("price=",bill)
print("Total bill=",bill)

