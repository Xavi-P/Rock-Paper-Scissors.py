import random
import os
play=True 
decision=""
decision2=""
ties=0
wins=0
loses=0
player=""
def player_count():
  print("Two modes: Player vs Player or Player vs computer")
  player=input("How many players?:1 or 2?:")
  while player != "1" and player != "2":
    print("invalid input please enter 1 or 2 to continue.")
    player=input("1 or 2?:")

  return int(player)

def get_user_choice():
  decision=input("rock,paper, or scissors?:")
  while decision != "rock" and decision != "paper" and decision != "scissors":
    print("invalid input please enter rock, paper, or scissors to continue.")
    decision=input("rock,paper, or scissors?:")
  return decision

def player2_choise():
  os.system('cls')
  print("Okay, player 2 what is your hand")
  decision2=input("rock,paper, or scissors?:")
  while decision2 != "rock" and decision2 != "paper" and decision2 != "scissors":
    print("invalid input please enter rock, paper, or scissors to continue.")
    decision2=input("rock,paper, or scissors?:")
  return decision2
  
def get_computer_choice():
  choises = ["rock", "paper", "scissors"]

  commputer_rand_choise=random.choice(choises)
  return commputer_rand_choise





def computer_results(player_hand,computer_hand,ties,loses,wins):

  if player_hand==computer_hand:
    print("it a tie")
    ties+=1
  elif player_hand=="rock" and computer_hand=="paper" or player_hand=="paper" and computer_hand=="scissors" or player_hand=="scissors" and computer_hand=="rock":
      print("you lose")
      loses+=1
      
  else:
      print("you win!")
      wins+=1
  print("ties:"+str(ties))
  print("wins:"+str(wins))
  print("loses:"+str(loses))
  print("would you like to play again?: y/n")
  choise=input()
  if choise=="y":
   return True,ties,wins,loses
  else: 
    print("Okay, better luck next time")
  return False,ties,wins,loses

def results1v1(player_hand,decision2,ties,loses,wins):

  if player_hand==decision2:
    print("it a tie")
    ties+=1
  elif player_hand=="rock" and decision2=="paper" or player_hand=="paper" and decision2=="scissors" or player_hand=="scissors" and decision2=="rock":
      print("Player 1, you lose")
      loses+=1
      
  else:
      print("Player 1 wins!")
      wins+=1
  print("ties:"+str(ties))
  print("wins:"+str(wins))
  print("loses:"+str(loses))    
  print("would you like to play again?: y/n")
  choise=input()
  if choise=="y":
   return True,ties,wins,loses
  else: 
    print("Okay, better luck next time")
  return False,ties,wins,loses
while play==True:
  player = player_count()
  player_hand=get_user_choice()
  if player==1:
    computer_hand=get_computer_choice()
    play, ties, wins, loses = computer_results(player_hand, computer_hand, ties, loses, wins)
  elif player==2:
    decision2 = player2_choise()
    play, ties, wins, loses=results1v1(player_hand,decision2,ties,loses,wins)
  
