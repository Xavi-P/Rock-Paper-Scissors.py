def results(player_hand,computer_hand):
  # if player_hand=="rock":
  #   print("fart")
  if player_hand==computer_hand:
    print("it a tie")
  elif player_hand=="rock" and computer_hand=="paper" or player_hand=="paper" and computer_hand=="scissors" or player_hand=="scissors" and computer_hand=="rock":
      print("you lose")
  else:
      print("you win")
   
results(player_hand,computer_hand)
