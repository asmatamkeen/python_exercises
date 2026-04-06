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