print("Welcome to Elijah's calculator!")

first_number = float(input("What is the first number of your equation?"))
second_number = float(input("What is the second number of your equation?"))
operation = input("Which basic operation would you like to use? (Addition, Subtraction, Multilpication, and Divison.)")

if operation == "Addition":
     print(first_number + second_number)
elif operation == "addition":
     print(first_number + second_number)
elif operation == "Subtraction":
     print(first_number - second_number)
elif operation == "subtraction":
     print(first_number - second_number)
elif operation == "Multiplication":
     print(first_number * second_number)
elif operation == "multiplication":
     print(first_number * second_number)
elif operation == "Divison":
     print(first_number / second_number)
elif operation == "divison":
     print(first_number / second_number)
else:
     print("Error. We don't support that operation yet.")
     
print("Copyright (c) 2025 Elijah Corwin")
