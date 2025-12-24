import random
play=True 
decision=""
ties=0
wins=0
loses=0
def get_user_choice(decision):
  decision=input("rock,paper, or scissors?:")
  while decision != "rock" and decision != "paper" and decision != "scissors":
    print("invalid input please enter rock, paper, or scissors to continue.")
    decision=input("rock,paper, or scissors?:")
  return decision

  

def get_computer_choice():
  choises = ["rock", "paper", "scissors"]

  commputer_rand_choise=random.choice(choises)
  return commputer_rand_choise





def results(player_hand,computer_hand,ties,loses,wins):

  if player_hand==computer_hand:
    print("it a tie")
    ties+=1
  elif player_hand=="rock" and computer_hand=="paper" or player_hand=="paper" and computer_hand=="scissors" or player_hand=="scissors" and computer_hand=="rock":
      print("you lose")
      loses+=1
      
  else:
      print("you win")
      wins+=1
      
  print("would you like to play again?: y/n")
  choise=input()
  if choise=="y":
   return True,ties,wins,loses
  else: 
    print("Okay, better luck next time")
  return False,ties,wins,loses

while play==True:
  computer_hand=get_computer_choice()
  player_hand=get_user_choice(decision)
  play, ties, wins, loses = results(player_hand, computer_hand, ties, loses, wins)
  print("ties:"+str(ties))
  print("wins:"+str(wins))
  print("loses:"+str(loses))
