#Dice rolling simulator
import random
print("Dice Rolling Simulator.\nPress 'Y' to Roll Dice and 'N' to stop.\n")
while True:                    
    ch = input("Roll Dice ?\n")
    if ch == 'Y' or ch == 'y':
        x = random.randint(1, 7)
        print(x)
    elif ch == 'N' or ch == 'n':
        break
    else:
        break
