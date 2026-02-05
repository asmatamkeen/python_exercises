name1=input("Enter your name:")
name2=input("Enter your lovers name:")
name1.lower()
name2.lower()
true=name1.count('t')+name2.count('t')+name1.count('r')+name2.count('r')+name1.count('u')+name2.count('u')+name1.count('e')+name2.count('e')
love=name1.count('l')+name2.count('l')+name1.count('o')+name2.count('o')+name1.count('v')+name2.count('v')+name1.count('e')+name2.count('e')
print(true)
print(love)
per=int(str(true)+str(love))
if per<10 or per>90:
    print(f"Your score is {per} and ou go together like coke and mentos")
elif per>=40 and per<=50:
    print(f"Your score is {per} and you are alright together")
else:
    print(f"Your score is {per}")

