#Rock Paper Scissors
import random
attempt = 0
win = 0
lose = 0

def quit():
    a = (input("You seem to be quitting, are you sure?: "))
    if a[0] == "y" or "Y":
      print("Alright! Hope to see you soon!")
      global attempt
      attempt = 0
      global win
      win = 0
      global lose
      lose = 0
      pass
    if a[0] == "n" or "N":
      print("Alright, have fun!")
      return rps2()

def stats():
  print(f"Wins: {win}")
  print(f"Losses: {lose}")
  rps2()

print("Rock Paper Scissors")
print("Quit by typing 'Quit'")
print("Check Stats with 'Data'")
def rps2():
  I = (input("Rock, Paper or Scissors?: "))  #user input
  capitalizedShape = I.capitalize()  #input check/spellcheck
  global attempt
  attempt = attempt + 1
  rps = random.randint(1, 3)  #computers choice
  if capitalizedShape[0] == "R":  #Rock
      print("You chose Rock")
      for x in range(1):
        if rps == 1:  #Duplicate
          print("Rock")
          print("Even, try again!")
          attempt
          return (rps2())
        elif rps == 2:  #Scissors
          print("Scissors")
          print("You win, try again!")
          print(f"Attempt: {attempt}")
          global win
          win = win + 1
          win
          print(f"Wins: {win}")
          return (rps2())
        elif rps == 3:  #Paper
          print("Paper")
          print("You lose, try again!")
          attempt
          global lose
          lose = lose + 1
          lose
          print (f"Losses: {lose}")
          print(f"Attempt: {attempt}")
          return (rps2())
  if capitalizedShape[0] == "S":
      print("You chose Scissors")
      for y in range(1):
          if rps == 1:
                print("Rock")  #Rock
                print("You lose, try again!")
                attempt
                lose = lose + 1
                lose
                print (f"Losses: {lose}")
                print(f"Attempt: {attempt}")
                return (rps2())
          elif rps == 2:
                print("Scissors")
                print("Even, try again!")
                attempt
                print(f"Attempt: {attempt}")
                return (rps2())
          elif rps == 3:  #Paper
                print("Paper")
                print("You win, try again!")
                attempt
                win = win + 1
                win
                print(f"Wins: {win}")
                print(f"Attempt: {attempt}")
                return (rps2())
  if capitalizedShape[0] == "P":
    print("You chose Paper")
    for z in range(1):
            if rps == 1:
                print("Rock")  #Rock
                print("You win, try again!")
                attempt
                win = win + 1
                win
                print(f"Wins: {win}")
                print(f"Attempt: {attempt}")
                return (rps2())
            elif rps == 2:  #Scissors
                print("Scissors")
                print("You lose, try again!")
                attempt
                lose = lose + 1
                lose
                print (f"Losses: {lose}")
                print(f"Attempt: {attempt}")
                return (rps2())
            elif rps == 3:  #Duplicate
                print("Paper")
                print("Even, try again!")
                attempt
                print(f"Attempt: {attempt}")
                return (rps2())
  if capitalizedShape[0] == "Q":
      quit()
  if capitalizedShape[0] == "D":
      stats()
  else:
      print("Try again!")
      return (rps2())
rps2()