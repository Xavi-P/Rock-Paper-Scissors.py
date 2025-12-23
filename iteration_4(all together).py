import random

decision=""
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
get_computer_choice()



player_hand=get_user_choice(decision)
computer_hand=get_computer_choice()



def results(player_hand,computer_hand):

  if player_hand==computer_hand:
    print("it a tie")
  elif player_hand=="rock" and computer_hand=="paper" or player_hand=="paper" and computer_hand=="scissors" or player_hand=="scissors" and computer_hand=="rock":
      print("you lose")
  else:
      print("you win")
   
results(player_hand,computer_hand)
