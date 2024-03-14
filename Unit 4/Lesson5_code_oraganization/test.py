 # Win conditions for user
  if user_choice == "Rock" and computer_choice == "Scissors" or \
       user_choice == "Paper" and computer_choice == "Rock" or \
       user_choice == "Scissors" and computer_choice == "Paper":
    return "You Win!"
  # Loss condition
  else:
    return "You Lose!"