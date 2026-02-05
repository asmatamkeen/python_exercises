import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images=[rock,paper,scissors]

user_choice=int(input("Enter your choice:(0-rock, 1-paper,2-scissors)"))
if user_choice>2 or user_choice<0:
    print("Invalid choice! Please enter correctly!!")
else:
    computers_choice=random.randint(0,2)
    print("you chose:")
    print(images[user_choice])
    
    print(f"computer chose:")
    print(images[computers_choice])
    if user_choice==computers_choice:
        print("Tie")
    elif (user_choice==0 and computers_choice==1) or (user_choice==1 and computers_choice==2) or (user_choice==2 and computers_choice==0):
        print("computer wins")
    else:
        print("YOU WIN")
