import avatar
import random

nose = random.randint(1,2)
mouth = random.randint(1,4)
bow_location = random.randint(1,3)

if bow_location == int(1):
    avatar.draw_bow()
elif bow_location == int(2):
    avatar.draw_eyes("medium")
else:
    avatar.draw_nose("button" if nose == 2 else "triangle")
    avatar.draw_mouth("teeth" if mouth == 1 else "neutral" if mouth == 2 else "smile")
    avatar.draw_bow()