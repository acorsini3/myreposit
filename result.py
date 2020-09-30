result = input("What is the result of 5+2? : ")

if result == "7":
    print("Congratulations!")

if result != "7":
    print("Try again !")
    result2 = input("What is the result of 5+2? : ")
    if result2 == "7":
        print("Congratulations!")
    if result2 != "7":
        print("Game over !")
