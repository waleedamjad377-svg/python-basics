import random

# Roll two six-sided dice.
exps = int(input("How many times you would like to repeat the experiment? "))
total = 0
exp = 1

while exp <= exps:
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)

    dice_sum = first_die + second_die
    total += dice_sum
    print("You rolled a " + str(dice_sum) + "!")
    exp += 1

avg = total/exps
print("The average is: " + str(avg))