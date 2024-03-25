from art import logo
import random
from replit import clear


def play_game():
  print(logo)
  print("Welcoem to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  guess = random.randint(1, 100)
  mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
  life = 0
  if mode == "easy":
    life = 10
  elif mode == "hard":
    life = 5
  print(f"You have {life} attemps remaining to guess the number.")

  while life != 0:
    guessNumber = int(input("Make a guess: "))
    if guess > guessNumber:
      print("Too low")
      print("Guess Again")
      life -= 1
    elif guess < guessNumber:
      print("Too high")
      print("Guess Again")
      life -= 1
    elif guess == guessNumber:
      print("You got it!")
      break

    print(f"You have {life} attemps remaining to guess the number.")

  if life == 0:
    print("You used all the attemps")
    print("You lost")


while input(
    "Do you want to play guessing the number game? type 'y' or 'n'") == 'y':
  clear()
  play_game()
