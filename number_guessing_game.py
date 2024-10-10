# Generate a random number
# Ask the user to make a guess
# If not a valid number
#  Print an error
# If number < guess 
#  Print too low
# If number > guess 
#  Print too high 
# Else 
#  Print well done 
import random 

best_score = None
while True:

   min_range = int(input("Enter min range: "))
   max_range = int(input("Enter max range: "))

   number_to_guess = random.randint(min_range, max_range )
   print(number_to_guess)

   guesses_left = 5
   attempts = 0

   
   while guesses_left > 0:
      guesses_left -= 1
      attempts += 1

      try:
         guess = int(input(f"Guess a number between {min_range} and {max_range}: "))

         if guess > number_to_guess:
            print("Too high! Try again")
            print(f"You have {guesses_left} left.")
               
         elif guess < number_to_guess:
            print("Too low! Try again.")
            print(f"You have {guesses_left} left.")

         else: 
            print(f"Congratulations! You guessed the number.")
            print(f"It took you {attempts} attempts to guess the number")
            
            
            if best_score is None or attempts < best_score:
               best_score = attempts
               print("This is your best score so far")
            else:
               print(f"Your best score is {best_score} attempts.")
            
            break

         if guesses_left == 0:
            print(f"You ran out of guesses. The correct number was {number_to_guess}.")
            if best_score:
               print(f"Your best score is still {best_score}")
            else:
               "No best score yet"
            break

      except ValueError: 
         print('Please enter a valid number')
   
   play_again = input("Do you want to play again y/n:").lower()
   if play_again != "y":
      if best_score:
         print(f"Thanks for playing! Your best score was {best_score}")
      else:
         print("Thanks for playing!")
      break










"""
number_to_guess = random.randint(1, 100)
while True:
   try:
      
      guess = int(input ('Guess the number between 1 and 100: '))
      if guess < number_to_guess:
         print("Too low! Try again.")
      elif guess > number_to_guess:
         print("Too high! Try again")
      else :
         print(f"Congratulations! You guessed the number.")
         break
   except ValueError:
      print('Please enter a valid number')

"""




"""
import random 

random_number = random.randint(1, 100)
print(random_number)
while True:
   user_guess = input("Guess the number (between 1 and 100): ")
   attempts = 0
   
   if int(user_guess) > random_number:
      attempts += 1
      print("Too high! Try again.")
      print(f"attempts = {attempts}")
      

   elif int(user_guess) < random_number:
      attempts += 1 
      print("Too low! Try again.")
      print(f"attempts = {attempts}")

   elif int(user_guess) == random_number:
      attempts += 1
      print(f"Congratulations! You guessed the number in {attempts} attempts")
      print(f"attempts = {attempts}")
      break
"""
