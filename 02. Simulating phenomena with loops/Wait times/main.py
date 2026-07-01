import random

num_cashiers = int(input("Enter the number of cashiers(1-4): "))
num_cooks = int(input("Enter the number of cooks(1-3): "))
total = 0


waiting_to_order = 0
waiting_for_food = 0

# Customers arrive every minute and line up to order.

for i in range(5*60):
    waiting_to_order = waiting_to_order + random.randint(0, 6)

# Each cashier can take up to two orders per minute.
    new_orders = min(num_cashiers * 2, waiting_to_order)
    

# After ordering, customers wait for their food to be made.
    waiting_to_order = waiting_to_order - new_orders
    waiting_for_food = waiting_for_food + new_orders

    num_serv = min(num_cooks, waiting_for_food)
    total += num_serv
    waiting_for_food -= num_serv
    
    print(str(waiting_to_order) + " customers waiting to order.")
    print(str(waiting_for_food) + " customers waiting for food.")

print("The total no. of customers served today from 12 to 5: " + str(total))