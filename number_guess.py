import random

number = random.randint(1, 10)

print ("Guess a number between 1 and 10. You will have a total of 3 guesses.")

guess1 = int(raw_input("Enter guess 1: "))
if(guess1 > number):
  print("Too high, try again.")
elif(guess1 < number):
  print("Too low, try again.")
else:
  print("You are correct! :)")
  exit()
  
guess2 = int(raw_input("Enter guess 2: "))
if(guess2 > number):
  print("Too high, try again.")
elif(guess2 < number):
  print("Too low, try again.")
else:
  print("You are correct! :)")
  exit()

guess3 = int(raw_input("Enter guess 3: "))
if(guess3 > number):
  print("Too high, game over!")
elif(guess3 < number):
  print("Too low, game over!")
else:
  print("You are correct! :)")
  


