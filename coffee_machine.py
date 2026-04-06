import sys

ingredients={
    'milk':500,
    'water':500,
    'coffee_grams':100
}

espresso={
    'milk':0,
    'water':50,
    'coffee_grams':18
}

latte={
    'milk':150,
    'water':50,
    'coffee_grams':18
}

cappuccino = {
    'milk':100,
    'water':250,
    'coffee_grams':24
}

menu={
    'espresso':espresso,
    'latte':latte,
    'cappuccino':cappuccino
}

cost={
    'espresso':120,
    'latte':180,
    'cappuccino':160
}

    


def order():
    profit=0
    while True:
        user_input=input("What would you like to have? (latte/ espresso / cappuccino):")
        if user_input in menu:
            recipe= menu[user_input]
            if user_input in cost:
                recipe_cost=cost[user_input]

                can_make = True
                for item in recipe:
                    if recipe[item] > ingredients[item]:
                        print(f"Sorry, there is not enough {item}.")
                        can_make = False
                        break
                
                if not can_make:
                    continue
                

                for item in recipe:
                    ingredients[item]=ingredients[item]-recipe[item]

            

                print(f"The price of {user_input} is {recipe_cost}")
                print("Please insert coins")
                coins_5=int(input(f"How many 5 Rs. coins:"))
                coins_10=int(input(f"How many 10 Rs. coins:"))
                coins_20=int(input(f"How many 20 Rs. coins:"))
                user_money= (coins_5*5) + (coins_10*10) + (coins_20*20)

                if user_money < recipe_cost:
                    print("Not enough money")
                    print(f"Here is your money Rs.{user_money}")
                    continue

                
                remaining_money=user_money-recipe_cost
                print(f"Here is your Rs.{remaining_money} in change")
                print(f"Here is your {user_input}")
                profit=profit +recipe_cost
        
        

        elif user_input == 'reload':
            ingredients['milk']= 500
            ingredients['water']= 500
            ingredients['coffee_grams']= 100
            print("The machine is reloaded")

        elif user_input == 'off':
            print("The machine is turned off")
            sys.exit(0)

        elif user_input == 'report':
            for item in ingredients:
                print(f"{item}:{ingredients[item]}")
            print(f"Money:{profit}")
                

            


        else:
            print("Sorry, Not on the menu")
            continue

        


    
    



order()
