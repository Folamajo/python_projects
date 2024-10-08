import random 
#PSEUDOCODE
#Loop - we want to put it in a loop so that the user can keep playing until the decide to stop
   #Ask: roll the dice
   #If user enters y 
   #  Generate two random numbers
   #  Print them
   #If user enters n
   #  Print thank you message
   #  Terminate
   #Else 
   #  Print invalid choice

#Ask: roll the dice

while True: 
   choice = input("Roll the dice? (y/n): ").lower()
   if choice == "y":
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
   elif choice == "n":
      print('Thanks for playing!')
      break
   else: 
      print('Invalid choice!')



#MY SOLUTION ORIGINAL 
"""
roll_dice = input("Roll the dice? (y/n):").lower() #makes the input lower case

dice = []
dice_numbers = [random.randint(1,6) for i in range(2)]

if roll_dice == "n":
   print ("Thanks for playing!")
elif roll_dice == "y":
   print(f"({', '.join(map(str, dice_numbers))})")
else: 
   print("Invalid choice!")

"""