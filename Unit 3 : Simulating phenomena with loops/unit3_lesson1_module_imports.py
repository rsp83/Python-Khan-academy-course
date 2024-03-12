# The above module is available on khan academy terminal.
import avatar
import random

nose = random.randint(1,2)
mouth = random.randint(1,4)
bow_location = random.randint(1,3)

if bow_location == int(1):
    avatar.draw_bow()
    avatar.draw_eyes("medium")
elif bow_location == int(2):
    avatar.draw_eyes("medium")
if nose == int(2):
    avatar.draw_nose("button")
else:
    avatar.draw_nose("triangle")
if mouth == int(1):
    avatar.draw_mouth("teeth")
elif mouth == int(2):
    avatar.draw_mouth("neutral")
else:
     avatar.draw_mouth("smile")
if bow_location == int(3):
    avatar.draw_bow()
