#set the secret number
import random
secret_number = random.randint(1,10)

#initializing attempt count
attempt = 5

#start the game
try:
    guess = input("Guess the secret number between 1 and 10 : ")
    while attempt>1:

        if int(guess) == int(secret_number):
            print("Congratulations")
            attempt = 0

        elif int(guess) < int(secret_number):
            attempt = attempt - 1
            print("The secret number is bigger")
            guess = input("Guess the secret number between 1 and 10 : ")

        elif int(guess) > int(secret_number):
            attempt = attempt - 1
            print("The secret number is smaller")
            guess = input("Guess the secret number between 1 and 10 : ")
        
    print("Game Over")

except:
  print("Couldn't convert your input to a valid number")
  quit()