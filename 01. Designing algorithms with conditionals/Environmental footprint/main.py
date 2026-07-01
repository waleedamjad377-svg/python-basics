footprint = 0
has_pet = input("Do you have a pet (yes/no)? ")
if has_pet == "yes":
    # Pets consume resources like water, litter, and toys. 
    footprint = footprint + 5
    meat = input("Does your pet's food contains meat (yes/no)? ")
    if meat == "yes":
        footprint += 10

days = int(input("How many days a week do you commute to school or work? "))
if days != 0:
    transport = input("Do you commute by foot, bike, bus, train, or car? ")
    if transport == "car":
        footprint = footprint + (8 * days)
    elif transport == "bus" or transport == "train":
        footprint += 4*days
    elif transport == "bike" or transport == "foot":
        footprint += days
        
print("Your environmental footprint score is " + str(footprint) + ".")
