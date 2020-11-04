a = "Hello, Nico!"
print(a[1])

a = "Hello, Nico!"
print(len(a))

a = "Hello, You!"
print(a[7:10])

a = "   Hello, You!   "
print(a.strip())

#upper lower
a = "Hello, You!"
print(a.lower())
print(a.upper())

#replace
a = "This is a snowy day"
b = a.replace("snowy", "sunny")
print(b)

#split
words = "apples,oranges,bananas"
fruits = words.split(",")
print(fruits)

a = "This is a great day to learn about programming."
b = a.find("great")
c = a.find("blue")

# b == 10
# c == -1

#combine
a = "This is a great day to learn about programming."
b = a.replace("great", "beautiful").upper().split(" ")

