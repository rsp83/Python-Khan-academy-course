# The above module is available on khan academy terminal.
import avatar
import random

nose = random.randint(1,2)

avatar.draw_bow()
avatar.draw_eyes("medium")
if nose == int(2):
    avatar.draw_nose("button")
else:
    avatar.draw_nose("triangle")
avatar.draw_mouth("smile")
