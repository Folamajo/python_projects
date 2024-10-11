import random 
import emoji 
rounds = 0   
computer_score = 0
user_score = 0

# while True:
while rounds < 3:
   user_choice = input ("Rock, paper, or scissors? (r/p/s): ").lower()
   
   choices = ('r', 'p', 's')
   emojis = {'r' :"👊", 'p': '📄', 's' : '✄' }
   computer_choice = random.choice(choices)
   


   try:
      if user_choice not in choices:
         raise ValueError

      print(f"computer chose {emojis[computer_choice]}")
      print(f"You chose {emojis[user_choice]}")


      if user_choice in choices:  
         if user_choice == computer_choice:
            print("Tie!")
            print(f"Current score: You {user_score} - {computer_score} Computer")
         elif \
            (user_choice == 'r' and computer_choice == 's') or \
            (user_choice == 'p' and computer_choice == 'r') or \
            (user_choice == 's' and computer_choice == 'p'):
            user_score += 1
            rounds += 1
            print("You win!")
            print(f"Current score: You {user_score} - {computer_score} Computer") 
         else:
            computer_score += 1
            rounds += 1
            print("You lose!")
            print(f"current scores: You {user_score} - {computer_score} Computer")
         
         if rounds == 3 or computer_score == 2 or user_score == 2:
            if user_score > computer_score:
               print(f"You win, the final score is: You {user_score} - {computer_score} Computer")
            elif computer_score > user_score: 
               print(f"You lose, the final score is: You {user_score} - {computer_score} Computer")
            break   
         
   except ValueError:
      print('Please enter rock (r), paper (p) or scissors (s).')










   # play_again = input("Do you want to play again (y/n): ").lower
   # if play_again != "y":
   #    print(f"Thanks for playing. The last score was {user_score} - {computer_score}")
   # else:
   #    print("Thanks for playing!")
   #    break