# first choice
choice1 = input("Do you want to convert something ? Y or N")
#second choice
while choice1 == "Y":
    choice2 = input("What do you want to convert ? celsius, CHF or liters ? ")
    #conversion
    if choice2 == "celsius" :
        celsius= input("Enter a tmperature in celsius :")
        farenheit = (celsius *9/5)+32
        print("the equivalent in farenheit is "+ farenheit)
        choice1 = input("Do you want to convert something ? Y or N")
    elif choice2 == "CHF" :
        CHF= input("Enter an amount in CHF :")
        EUR = (CHF *0.93)
        print("the equivalent in EURO is "+ EUR)
        choice1 = input("Do you want to convert something ? Y or N")
    elif choice2 == "liters" :
        liters= input("Enter a quantity in liters :")
        galons = (liters *0.264)
        print("the equivalent in galons is "+ galons)     
        choice1 = input("Do you want to convert something ? Y or N")   


