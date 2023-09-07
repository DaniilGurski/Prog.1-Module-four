import os
import math
import random

os.system("cls")


# uppgift 1
def getValidInput(prompt): 
    while True: 
        try: 
            user_input = int(input(prompt))
            break
        except:
            print("Your input type is not valid !")
    return user_input

def checkLength(length):
    if length < 140 or length > 205:
        return "Unfortunately you can't ride this attraction :("
    return "Welcome aboard !"


length = getValidInput("Enter your length: ")
print(checkLength(length))


# uppgift 2
def welcomeProgram():
    name = input("Whats your name ?: ")
    age = getValidInput("How old are you ?: ") # funktion från uppgift 2 som ser till att input är en heltal.

    if age > 18: 
        return f"Hello Mr.{name}"
    return f"Hello {name}"

print(welcomeProgram())


# uppgift 3
weight = getValidInput("enter your weight: ")
height = getValidInput("enter your height: ")

print("your BMI is : %s" %(weight / (height / 100) ** 2))


# uppgift 4
circle_radius = getValidInput("enter radius of your circle: ")
    
result = (circle_radius * circle_radius) * math.pi
print(f"{circle_radius}^2 * pi  = {result} (area)")


# uppgift 5
first_number = getValidInput("Enter your first number: ")
second_number = getValidInput("Enter your second number: ")

print(
    """
    Select an operation to perform.
    (+) for addition
    (-) for subtraktion
    (*) for multiplication
    (/) for division
    """
)

while True:
    selected_operation = input("")

    if selected_operation == "+":
        print(first_number + second_number)
        break
    elif selected_operation == "-":
        print(first_number - second_number)
        break
    elif selected_operation == "*":
        print(first_number * second_number)
        break
    elif selected_operation == "/":
        print(first_number / second_number)
        break
    else:
        print("unknown operation.")
        continue


# uppgift 6
dice_value = random.randint(1,6)
print(f"You rolled a dice and got {dice_value}")


# uppgift 7
thow_number = getValidInput("How many dices do you want to roll?: ")

for i in range(thow_number):
    dice_value = random.randint(1,6)
    print(f"You got {dice_value} for the roll {i + 1}")




    
        
    




