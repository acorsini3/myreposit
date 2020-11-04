for x in range(4):
    current_step = str(x + 1)
    if current_step == "1":
        print(current_step + " step")

    else:
        print(current_step + " steps")


for y in range(4):
    current_step = str(y + 1)
    step_word = " "
    if current_step == "1":
        step_word = " step"
    else:
        step_word = " steps"
    print("It's " + current_step + step_word)

for z in range(10):
    print(z)

my_number=0

while my_number<10:
    print(my_number)
    my_number=my_number+1
