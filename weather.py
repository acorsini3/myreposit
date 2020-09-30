weather = input("What is the weather like ? Sunny or Rainy : ")
temperature = input("What is the temperature ? Cold or Hot ? : ")

if weather == "Sunny" and temperature == "Hot":
    print ("Take your sunglasses !")

elif weather == "Rainy" and temperature == "Cold":
    print ("Take your umbrella !")

else:
    print ("That's strange !")