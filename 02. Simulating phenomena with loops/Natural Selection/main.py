"""Simulates natural selection in the fictional Neebler population."""

import random

# Starting population with each trait variation.
small_neeblers = 20
big_neeblers = 80



for generation in range(50): 

    if big_neeblers == 0:
        print("Big Neeblers got extinct")
    
    if big_neeblers==0 and small_neeblers  == 0:
        print("Both got extinct")
        break
    if small_neeblers == 0:
        print("Small Neeblers got extinct")
    print("For Generation " + str(generation+1))
    baby_big_neeblers = 0
    baby_small_neeblers = 0
    
    for neebler in range(small_neeblers):
        # Low chance of being spotted by predators since they're small.
        chance_of_being_spotted = random.randint(0, 4)
        if chance_of_being_spotted == 4:
            small_neeblers = small_neeblers - 1
    
    for neebler in range(big_neeblers):
        # high chance of being spotted by predators since they're big.
        chance_of_being_spotted = random.randint(2, 4)
        if chance_of_being_spotted == 4:
            big_neeblers = big_neeblers - 1
    
    for neebler in range(small_neeblers):
        # Smallness trait gets passed to their babies.
        num_babies = random.randint(0, 3)
        baby_small_neeblers = baby_small_neeblers + num_babies
    
    for neebler in range(big_neeblers):
        # bigness trait gets passed to their babies.
        num_babies = random.randint(0, 3)
        baby_big_neeblers = baby_big_neeblers + num_babies

    # Babies become the starting population of the next generation.
    small_neeblers = baby_small_neeblers
    big_neeblers = baby_big_neeblers
    
    print(str(small_neeblers) + " small Neeblers")
    print(str(big_neeblers) + " big Neeblers")
