employees = ["Richard Swift", "Marie-Anne Petrie"]
number_of_employees = len(employees)
message = "At the beginning, there are " + str(number_of_employees) + " employees."
print(message)
print(employees)

employees.append("Cody Lightfoot")
employees.append("Laure Simmons")

number_of_employees = len(employees)
message = "The company grows and now has " + str(number_of_employees) + " employees."
print(message)
print(employees)

employees.pop(1)

number_of_employees = len(employees)
message = "Marie-Anne left the company. There are now " + str(number_of_employees) + " employees."
print(message)
print(employees)