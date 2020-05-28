#Guessing random number
import random
n = random.randint(0, 20)
x = int(input("Enter a number :\n"))
while True:
    if n < x:
        print("The number is less than ", x)
        x = int(input("Guess again :\n"))
    elif n > x:
        print("The number is greater than ", x)
        x = int(input("Guess again :\n"))
    else:
        print("\nCongratulations !\nCorrect Guess !!")
        break
