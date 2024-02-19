import random

running_total = 0

i = 1
while i <= 10 :
   first_die = random.randint(1, 6)
   second_die = random.randint(1, 6)

   dice_sum = first_die + second_die
   print("You rolled a " + str(dice_sum) + "!")
   running_total += dice_sum
   i += 1

average = running_total / 10 
print ("Average of " + str(average))