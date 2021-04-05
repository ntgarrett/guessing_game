# guessinggame.py
import random

# Game function
def guessingGame():
  difficulties = [[1,10], [1,100], [1,1000], [1,10000]]
  guess = 0
  count = 0
  difficultyChoice = -1
  found = False

  print("\n" + ("-" * 56))
  print("Guessing game! How many tries to guess the right number?")
  print("-" * 56)
  while difficultyChoice < 0: 
    print("\nEnter a difficulty level:\n1 -> 1 to 10\n2 -> 1 to 100\n3 -> 1 to 1000\n4 -> 1 to 10000\n")
    temp = input("Difficulty: ")
    if temp.isdigit():
      if int(temp) == 0:
        exit()
      if 0 < int(temp) < 5:
        difficultyChoice = int(temp)

  numToGuess = random.randrange(difficulties[difficultyChoice - 1][0], difficulties[difficultyChoice - 1][1])
  print(f"Our range is from [{difficulties[difficultyChoice - 1][0]} to {difficulties[difficultyChoice - 1][1]}]! I've chosen a random number in this range. Start guessing!\n")

  while not found:
    guess = input("Guess: ")
    if guess.isdigit():
      if int(guess) == 0:
        exit()
      elif int(guess) < numToGuess:
        print("Nope! Higher...")
        count += 1
      elif int(guess) > numToGuess:
        print("Nope! Lower...")
        count += 1
      else:
        count += 1
        print(f"\nYes! The number was {numToGuess}!")
        if count == 1:
          print(f"You found the number in ({count}) try. Amazing!\n")
        else:
          print(f"You found the number in ({count}) tries.\n")
        found = True

# Program loop
while True:
  print("-" * 32)
  print("Menu options:\n\n0 -> Exit program (at any time)\n1 -> Start new guessing game")
  print("-" * 32)
  inp = input("Option: ")
  if inp.isdigit():
    if int(inp) == 0:
      exit()
    elif int(inp) == 1:
      guessingGame()
  
