# Hackbright-Scholarship
# Pasted from https://repl.it/@CodeHotPink/Game-Box-for-Scholarship
# This is my first time using GitHub. I'm still learning how to use it. If it doesn't work try the repl.it 
# ¯\_(ツ)_/¯

""" Program that has different games to user to play.
Hangman
Rock Paper Scissors
Pig (Dice Game)

Pseudocode:
print greeting
ask user which game they would like to play?
  if user choice == game1:
    ask if they need directions
    play game
    play again or main menu?
  repeat for other 2
"""
from time import sleep
from random import choice
from random import randint

def main_menu():
  print("Your game options are:")
  sleep(1)
  print("1. Hangman")
  sleep(1)
  print("2. Pig (Dice Game)")
  sleep(1)
  print("3. Rock, Papers, Scissors")
  sleep(2)
  print()
  print("Which game would you like to play?")
  print("Enter the number of which game you would like to play")
  while True:
    try:
      game_option = int(input("> "))
      print()
      if game_option == 1:
        print("You have chosen Hangman!")
        sleep(1)
        game_directions(game_option)
        while True:
          hangman_game()
          play = play_again()
          if play is False:
            break
        exit_or_menu()
        break
      elif game_option == 2:
        print("You have chosen Pig!")
        sleep(1)
        game_directions(game_option)
        while True:
          pig_game()
          play = play_again()
          if play is False:
            break
        exit_or_menu()
        break
      elif game_option == 3:
        print("You have chosen Rock, Paper, Scissors!")
        sleep(1)
        game_directions(game_option)
        while True:
          rock_paper_scissors_game()
          play = play_again()
          if play is False:
            break
        exit_or_menu()
        break
      else:
        print("Please choose from 1 - 3.")        
    except ValueError:
      print("Please enter the number of which game you would like to play.")

def yes_or_no():
  print("Enter yes or no.")
  while True:
    yes_no = input("> ").lower()
    if yes_no.startswith("y"):
      print()
      return True
    elif yes_no.startswith("n"):
      print()
      return False
    else:
      print("Invalid. Enter yes or no.")

def game_directions(game_option):
  print("Do you need the rules and directions of the game?")
  need_rules = yes_or_no()
  if need_rules is True:
    if game_option == 1:
      hangman_directions()
    elif game_option == 2:
      pig_directions()
    elif game_option == 3:
      rock_paper_scissors_directions()
  else:
    print("You will now be directed to the game.")
    sleep(2)
    print()

def exit_or_menu():
  print("Would you like to go back to the menu to play another game?")
  sleep(1)
  play_or_exit = yes_or_no()
  if play_or_exit is True:
    print("You'll now be redirected back to the main menu.")
    print()
    sleep(2)
    main_menu()
  else:
    print("Thank you for playing!")

def play_again():
  print("Do you want to play again?")
  again = yes_or_no()
  return(again)



#############################################################
#############################################################
################     Hangman Game Code       ################
#############################################################
#############################################################

def hangman_directions():
  print("You are a given a word's length.")
  sleep(1)
  print("You guess the word by letter.")
  sleep(1)
  print("If the letter is in the word, the word will reappear where it belongs.")
  sleep(1)
  print("For example, you guessed \"i\" for the word \"pie\".")
  sleep(1)
  print("It will print \"-i-\".")
  sleep(1)
  print("If the letter is not in the word, you lose a try.")
  sleep(1)
  print("You will have a total of 7 tries to guess the word.")
  sleep(2.5)
  print("You will now be directed to the game.")
  sleep(2)

def hangman_category():
  """ 
  Have the user select category and difficulty
  Ask which category of words
    cowboys/old western or futureistic/sci-fi
  """
  print("Which category would you like to play?")
  sleep(1)
  while True:
    print("Western or Sci-Fy?")
    category = input("> ").lower()
    print()
    if category.startswith("w"):
      sleep(1)
      return("western")
    elif category.startswith("s"):
      sleep(1)
      return("scifi")
    else:
      print("Invalid Entry. Please select category.")
      sleep(1)

def hangman_difficulty():
  """Ask which difficulty
  easy = 3 - 5 lettered words
  medium = 6 - 8 lettered words
  hard = 9+ lettered words
  """
  print("You have the option of easy (3 - 5 letters), medium (6 - 8 letters) or hard (9+ letters).")
  sleep(1.5)
  while True:
    print("Which level do you want?")
    difficulty = input("> ").lower()
    print()
    if difficulty.startswith("e"):
      return("easy")
      print()
      sleep(1)
    elif difficulty.startswith("m"):
      return("medium")
      print()
      sleep(1)
    elif difficulty.startswith("h"):
      return("hard")
      print()
      sleep(1)
    else:
      print("Invalid Entry. Please select difficulty.")
      sleep(1)

def hangman_show_answer(answer, guessed):
  word = ""
  for i in answer:
    if i in guessed:
      word += i
    else:
      word += "-"
  return(word)

def hangman_guessing(answer, guessed):
  """  
  Actual game play
  Have the user guess a letter
    if letter is in the answer:
        print correct!
        show word with correct letter showing but others dashed out
        check if word is complete or not
    else:
        print wrong!
        put wrong letter in dictionary to track
  print congratulations if won
  ask user if they want to play again 
  """
  tries = 7
  word = hangman_show_answer(answer, guessed)
  print("Your word is {}!".format(word))
  print("There are {} letters in {}.".format(len(word),word))
  sleep(1.5)
  while tries > 0:
    print()
    sleep(1)
    print("Guess a letter:")
    guess = input("> ").lower()
    print()
    if guess in guessed:
      print("You have already guessed that letter. Try again.")
    elif guess in answer:
      print("Correct! {} is in the word!".format(guess))
      guessed[guess] = 1
      word = (hangman_show_answer(answer,guessed))
      hangman_winner = hangman_check_winner(word,answer)
      if hangman_winner is True:
        break
      else:
        print("The word is {}".format(word))
    elif guess.isalpha() is False:
      print("Invalid. Guess a letter.")
    else:
      tries -= 1
      guessed[guess] = 1
      print("Incorrect. {} is not in the word.".format(guess))
      print("The word is {}".format(word))
      print("You have {} tries left.".format(tries))
      hangman_show_answer(answer,guessed)
      if tries == 0:
        sleep(2)
        print("Darn it, that was your last try.")
        print("You lose.")
        print("The word was \"{}\".".format(answer))
        print()
        sleep(1)
      else:
        pass
      
def hangman_check_winner(word, answer):
  if word == answer:
    sleep(1)
    print()
    print("The word is {}!".format(word))
    print("Congratulations, you've won!")
    print()
    sleep(1)
    return True
  else:
    return False
  

def hangman_game():
  category = {
    "western":{"easy":["cow","boots","gun","horse","gang","wild","dust","west","howdy"],"medium":["cahoots","calvary","campfire","leather","robbery","uncivil","tombstone","justice"],"hard":["rebellious","treacherous","california","backslapping","final frontier","indigenous","notorious"]},
    "scifi":{"easy":["alien","moon","space","comet","beam","robot","atom", "scotty","portal","galaxy"],"medium":["android","blaster","planet","rocket","science","klingon","stargate","infinity","universe"],"hard":["death ray","use the force","millennium falcon","spaceship","interstellar","enterprise","extraterrestrial","astronaut"]}
    }
  
  guessed = {" ":1}
  cat = hangman_category()
  lev = hangman_difficulty()
  answer = choice(category[cat][lev])
  hangman_guessing(answer, guessed)
  

#############################################################
#############################################################
###############     Pig Dice Game Code       ################
#############################################################
#############################################################

def pig_directions():
  print("The goal is to reach 25 points.")
  sleep(1.5)
  print("The game is played in rounds. First yours, then the computer's.")
  sleep(2)
  print("You will roll one die. If you roll a '1', you lose your turn AND points.")
  sleep(2)
  print("If you land on any other number you have the choice to roll again or hold your points and pass to the computer.")
  sleep(3.5)
  print("You will now be directed to the game.")
  sleep(2)


def rounds(pts, cts, pp, cp):
  while pts <= 25 and cts <= 25:
    print()
    print("It's your turn.")
    sleep(1)
    prp = player_round(pts, pp)
    # prp is player's round points while calling the player's turn at the same time
    if prp >= 25:
      #player_round returns the total score user has that's why we check if it's >= 25
      sleep(1)
      print()
      return True
    else:
      pts += prp
      print("Your total score is {}.".format(pts))
      print()
      sleep(2)
      print("It's now the computer's turn.")
      sleep(1)
      cts += computer_round(cts,cp)
      print()
      if cts >= 25:
        sleep(1)
        return True
      print("The computer's total score is {}.".format(cts))
      sleep(2)

def player_round(pts, pp):
  player_roll = randint(1,6)
  print("Your roll is {}!".format(player_roll))
  sleep(1)
  if player_roll == 1:
    print("You have lost your turn and points.")
    pp = 0
    # player points.
    print()
    sleep(2)
    return pp
  else:  
    pp += player_roll
    win = pig_check_winner(pts,pp,0,0)
    """ I check if there is a winner during the round in case if player does not realize that they won. The program auto checks for them."""
    if win == None:
      print("Would you like to roll again?")
      roll_again = yes_or_no()
      sleep(1)
      if roll_again is True:
        return player_round(pts,pp)
      else:
        return pp
    elif win >= 25:
      return win
      
def pig_check_winner(pts, pp, cts, cp):
  #calculates the total scores to see if over 25
  pts += pp
  cts += cp
  if pts >= 25:
    print("Your total score is {}!".format(pts))
    sleep(1)
    print("Congratulations, you've won!")
    return pts
  elif cts >= 25:
    print("The computer's total score is {}!".format(cts))
    sleep(2)
    print("Darn it, the computer made it to 25 before you.")
    sleep(1)
    print("You lose.")
    return cts
  # Returns none if no one wins

def computer_round(cts, cp):
  computer_roll = randint(1,6)
  print("The computer rolled {}.".format(computer_roll))
  sleep(1)
  if computer_roll == 1:
    print("The computer has lost it's turn and points.")
    cp = 0
    sleep(2)
    return cp
  else:
    cp += computer_roll
    win = pig_check_winner(0,0,cts,cp)
    if win == None:
      if choice(["yes","no"]) == "yes":
        print("Computer will roll again.")
        sleep(1)
        return computer_round(cts,cp)
      else:
        print("The computer chose to hold its points.")
        return cp
    elif win >= 25:
      return win

def pig_game():
  pts = 0
  # player total score
  pp = 0
  # player points
  cts = 0
  # computer total points
  cp = 0
  # computer points
  rounds(pts, cts, pp, cp)


  #############################################################
#############################################################
################     Rock, Paper, Scissors       ################
#############################################################
#############################################################

def rock_paper_scissors_directions():
  print("You chose rock, paper, scissors.")
  sleep(1)
  print("Rock breaks scissors.")
  sleep(1)
  print("Paper covers rock")
  sleep(1)
  print("Scissor cuts paper.")
  sleep(2.5)
  print("You will now be directed to the game.")
  sleep(2)

def rock_paper_scissors_winner(player_move,computer_move):
  if player_move == computer_move:
    print("{} and {}?!".format(player_move,computer_move))
    print("It's a tie!")
    sleep(1)
  elif player_move == "Rock":
    if computer_move == "Scissors":
      print("{} beats {}!".format(player_move,computer_move))
      print("Congratulations, you've won!")
      sleep(1)
    else:
      print("{} beats {}!".format(computer_move,player_move))
      print("Darn it, you lost.")
      sleep(1)
  elif player_move == "Paper":
    if computer_move == "Rock":
      print("{} beats {}!".format(player_move,computer_move))
      print("Congratulations, you've won!")
      sleep(1)
    else:
      print("{} beats {}!".format(computer_move,player_move))
      print("Darn it, you lost.")
      sleep(1)
  elif player_move == "Scissors":
    if computer_move == "Paper":
      print("{} beats {}!".format(player_move,computer_move))
      print("Congratulations, you've won!")
      sleep(1)
    else:
      print("{} beats {}!".format(computer_move,player_move))
      print("Darn it, you lost.")
      sleep(1)

def rps_return_move(move):
  move_choices = {"1":"Rock","2":"Paper","3":"Scissors"}
  for i in move_choices:
    if i == move:
      return(move_choices[i])

def rock_paper_scissors_game():
  print("""Which number will you choose:
  1. Rock
  2. Paper
  3. Scissors""")
  player_move = input("> ")
  player_move = rps_return_move(player_move)
  computer_move = choice(["1","2","3"])
  computer_move = rps_return_move(computer_move)
  sleep(.5)
  print("{} vs {}".format(player_move,computer_move))
  sleep(1)
  rock_paper_scissors_winner(player_move,computer_move)
  print()

def game_box():
  print("Welcome to Marcella's Box of Games!")
  sleep(1)
  main_menu()

game_box()

