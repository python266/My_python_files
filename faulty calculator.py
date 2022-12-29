print("__--__Welcome to Calculator__--__")
#faulty calculator
#user choice
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Division")
#user Input
user = input("Enter you choice: ")
#user giving her number
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your secound number: "))
#conditional statement
#add
if user == "Add":
    print("Your number is: ", num1 - num2)
#subtration
elif user == "Sub":
    print("Your answer is: ", num1 + num2)
#multiplication
elif user == "Multiply":
    print("Your answer is: ", num1 / num2)
#division
elif user == "Division":
    print("Your answer is: ", num1 ** num2)
else:
    x = input()
    print("Press 'Enter' key to exit: ", x)
print("Thank you")