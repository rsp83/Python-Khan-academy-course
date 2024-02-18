import random

i = 1
while i <= 10 :
   first_die = random.randint(1, 6)
   second_die = random.randint(1, 6)

   dice_sum = first_die + second_die
   print("You rolled a " + str(dice_sum) + "!")
   i += 1