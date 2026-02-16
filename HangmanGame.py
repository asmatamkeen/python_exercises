from wonderwords import RandomWord
print("Let's play Hangman!")
comp_word=RandomWord().word().lower()
word_length=len(comp_word)
guessed_word=['_']*word_length
print("You have only 6 lives so try to guess thhe word within 6 attemps! Good luck!")
print(guessed_word)
chance=6
print(guessed_word)
while True:
    if guessed_word==list(comp_word):
        
        print("You win")
        break
    elif chance==0:
        print(f"You lose. The word was {comp_word}")
        break
    else:
        if chance>0:
            letter=input("Guess a letter:")
            if letter in comp_word:
                if letter in guessed_word:
                    chance=chance-1
                    print(f"The letter is already guessed. You lose a chance. chances left are {chance}")
                    continue
                else:
                    for i, ch in enumerate(comp_word): 
                        if ch==letter:                 
                            guessed_word[i]=letter
                print(f"You guessed it right.\n{guessed_word}")
            else:
                chance=chance-1
                print(f"You guessed it wrong. You lose a chance.\nChances left are {chance}") 



        else:
            break




    
