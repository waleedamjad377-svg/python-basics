import virus

population = int(input("Enter the population of chicken(100-1000000): "))
infected = int(input("Enter the no. of infected chickens in beginning: "))
can_catch_virus = population - infected
contacts_per_day = int(input("Enter the no. of contacts a chicken makes per day(5-15): "))
rec = 0

for day in range(90):
    # Infected chickens spread the virus to those who haven't already had it.
    
    if day >= 14:
        contacts_per_day = 3

    
    newly_infected = virus.spread(
        infected, can_catch_virus, population, contacts_per_day
    )
    
    infected = infected + newly_infected 
    rec = virus.recover(infected)
    infected -= rec
    if infected <= 0 or infected >= population:
        break
    can_catch_virus = can_catch_virus - newly_infected
    
    print(str(infected) + " chickens infected.")
    
print("----------")
print(str(population - can_catch_virus) + " chickens caught the virus.")
