import random

money = 100

#Write your game of chance functions here

def coin_flip(guess, bet):
  if bet <= 0:
    print("Your balance is 0, Please top-up!")
    return 0
    print("Best of Luck!")
    
  #save the random number in a varaiable num
    print("The number you have guessed " + guess)
  num = random.randint(1, 2)
  print(num)
  print(guess)


  if (guess.lower() == "heads" and num == 1) or (guess == "tails" and num == 2):
    print("You have won" + str(bet) + ". Now your balance " + str(money + bet))
    return bet
  else:
    print("Sorry, You lost " + str(bet) + "Now your balance " + str(money - bet))
    return -bet




def Cho_han(guess, bet):
  if bet <= 0:
    print("Your balance is 0, Please top-up!")
    return 0
    print("Best of Luck!")

  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  total = dice1 + dice2

  print(total % 2)

  if (guess.lower() == "even" and total % 2 == 0) or (guess.lower() == "odd" and total % 2 == 1):
    print("Congratulations, You have won " + str(bet) + "£. Now your Balance is " + str(money + bet))
    return bet
  else:
    print("Sorry, You  " + str(bet) + "£. Now your Balance is " + str(money - bet))
    return -bet



def card(bet):
  if bet <= 0:
    print("Your balance is 0, Please top-up!")
    return 0
    print("Best of Luck!")
  player1 = random.randint(1, 13)
  player2 = random.randint(1, 13)

  print ("Player1 card is " + str(player1))
  print ("Player2 card is " + str(player2))

  if player1 > player2 :
      print("Congratulations, You have won " + str(bet) + "£. Now Your Balance is " + str(money + bet))
      return bet
  elif( player1 < player2):
      print("Sorry, You have lost " + str(bet) + "£. Now your Balance is " + str(money - bet))
      return -bet
  else:
      print("It is a Tie")
      return 0

def roulette(guess, bet):
  if bet <= 0:
    print("Your balance is 0, Please top-up!")
    return 0
    print("Best of Luck!")
  result = random.randint(0,37)
  print("Player guessed " + str(guess) + ", Ball landed on " + str(result))
  print(result % 2)
  if (guess == "Odd" or guess == "odd") and (result%2 == 1 ):
    print("Player was right and wins £"+str(bet))
    return bet
  if (guess == "Even" or guess == "even") and (result%2 == 0):
    print("Player was right and wins £"+str(bet))
    return bet
  if guess == result:
    print("Player was correct and wins £" + str(bet*35))
    return bet*35
  else:
    print("Player was incorrect and loses £" + str(bet))
    return -bet

money += coin_flip("Heads", 10)
money += Cho_han("Odd", 5)
money += card(10)
money += roulette("Even", 10)

print(money)
#Call your game of chance functions here
