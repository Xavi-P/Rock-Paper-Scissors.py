import random

decision=""
def get_user_choice(decision):
  decision=input("rock,paper, or scissors?:")
  while decision != "rock" and decision != "paper" and decision != "scissors":
    print("invalid input please enter rock, paper, or scissors to continue.")
    decision=input("rock,paper, or scissors?:")
  return decision

  
decision=get_user_choice(decision)
# to test
print(decision)

def get_computer_choice():
  choises = ["rock", "paper", "scissors"]
  # to test
  print(random.choice(choises))
get_computer_choice()
