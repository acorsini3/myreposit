def convert():
    celsius = int(input("What is the temperature in celsius today? "))
    farenheit = (celsius * 9/5) + 32
    message = "the equivalent in farenheit is " + str(farenheit)
    print(message)
convert()