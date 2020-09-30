secret_word = "kiwi"
guess = input("What is my secret word ? : ")

if secret_word == guess.lower():
    print("Congratulations! You've found the secret word !")

if secret_word != guess.lower():
    print("You can play again.")