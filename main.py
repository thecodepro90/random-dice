import random

numofdice = int(input("Number of dice: "))
dice = 0
if numofdice > 10:
    print("Too many dice!")
else:
    for dicenum in range(numofdice):
        dicenum = random.randint(0,6)
        dice+=1
        print(f"Dice {dice}: {dicenum} ")

