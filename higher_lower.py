import game_db
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    a, b= 0,1
    count=0
    while True:
        if b >= len(game_db.data):
            print(f"You've beaten the game! Final score: {count}")
            break
        
        choice1=game_db.data[a]
        choice2=game_db.data[b]
        print(f"Compare 1: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
        print(game_db.vs)
        print(f"\nCompare 2: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")
        user_input=int(input("Who has more followers? Type '1' or '2':"))
        if user_input==1:
            user_choice=choice1
        else:
            user_choice=choice2

        if user_choice == choice1:
             other_choice= choice2

        else:
             other_choice=choice1

        if user_choice['follower_count'] > other_choice['follower_count']:
            a = b
            b= b+1
            count = count+1
            clear_screen()
             
            print(f"You are right. Your score is {count} ")

        

             
        else:
             clear_screen()
             print(f"You are wrong. Your final score is {count}")
             break
        


game()
        