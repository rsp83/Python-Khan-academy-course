import random

running_total = 0
repeat = int(input("How many times you would like to repeat the experiment ? "))

i = 1
while i <= repeat :
   first_die = random.randint(1, 6)
   second_die = random.randint(1, 6)

   dice_sum = first_die + second_die
   print("You rolled a " + str(dice_sum) + "!")
   running_total += dice_sum
   i += 1

average = running_total / repeat 
print ("Average of " + str(average))