def conv(eur):
    msg1 = " eur is worth "
    msg2 = " usd"
    result = eur * 1.1738
    return str(eur) + msg1 + str(result) + msg2

user_input = input("How much euros would you like to exchange ? ")
conversion = conv(float(user_input))

print(conversion)

if float(user_input) > 10000:
    print("It's alot of money!")