import os
print("*****Welcome to The Silent Auction Program*****")
bidders={

}
def add_bidder():
    name=input("What is your name:")
    bid=int(input("What is your bid?:"))
    bidders[name]=bid

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


add_bidder()

while True:
    user_input=input("Are there any other bidders? Type 'yes' or 'no':")
    if user_input=='yes':
        clear_screen()
        add_bidder()
    
    else:
        for name,bid in bidders.items():
            winning_bid=max(bidders.values())
            target=winning_bid
            if bid == target:
                winner=name
        print(f"The  winner is {winner} with a bid of {winning_bid}")
        break
