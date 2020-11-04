#set the secret number

import random
secret_number = random.randint(1,10)

#initializing attempt count
attempt = 5

#start the game

guess = input("Guess the secret number between 1 and 10 : ")
while attempt>0


    if int(guess) == secret_number
        print("Congratulations")
        print("You found the secret numer in " + attempt + "attempt")

    elif int(guess1) < secret_number 
        attempt = attempt + 1
        print("The secret number is bigger")
        print("Try again")

    elif int(guess1) > secret_number 
        attempt = attempt + 1
        print("The secret number is smaller")
        print("Try again")
        
print("Game Over")