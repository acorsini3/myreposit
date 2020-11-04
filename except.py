number = input("Type a number: ")

try:
  result = int(number) + 1
except:
  print("Couldn't convert your input to a valid number")
  quit()

print("The result is " + str(result))