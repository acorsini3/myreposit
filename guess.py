guess1 = input("I choose a number between 1 and 10, guess which one : ")
guess2 = input("I choose a colour, guess which one : ")

secret_number = "3"
secret_colour = "red"

if guess1 == secret_number and guess2 == secret_colour:
    print("Amazing! You found both !")

elif guess1 == secret_number and guess2 != secret_colour:
    print("Congrats ! You found the right number but not the colour")

elif guess1 != secret_number and guess2 == secret_colour:
    print("Congrats ! You found the right colour but not the number")

elif guess1 != secret_number and guess2 != secret_colour:
    print("Try again")

