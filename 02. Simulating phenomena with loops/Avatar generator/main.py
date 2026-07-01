import avatar
import random

numbow = random.randint(1, 3)
if numbow == 1:
    avatar.draw_bow()


avatar.draw_eyes("medium")

numnos = random.randint(1, 2)
if numnos == 1:
    avatar.draw_nose("triangle")
else:
    avatar.draw_nose("button")

nummouth = random.randint(1, 4)
if nummouth == 1 or nummouth == 2:
    avatar.draw_mouth("smile")
elif nummouth == 3:
    avatar.draw_mouth("neutral")
else:
    avatar.draw_mouth("teeth")

if numbow == 2:
    avatar.draw_bow()
