print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Where would you like to go?")
left_or_right = input("Type 'left' or 'right'\n").lower()

if left_or_right == "left":
    print("You have reached a river. Would you like to swim or wait")
    swim_or_wait = input("Type 'swim' or 'wait'\n").lower()
    if swim_or_wait == "wait":
        print("you have reached three doors. Which door would you like to go through!")
        choose_door = input("Type 'red' or 'blue' or 'yellow \n").lower
        if choose_door == 'red':
            print("Burned by fire. Game Over")
        elif choose_door == 'blue':
            print("Eaten by beasts. Game Over.")
        elif choose_door == 'yellow':
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over")
elif left_or_right == "right":
    print("You fell in a hole. Game over.")
else:
    print("Error: please choose 'left' or 'right'" )