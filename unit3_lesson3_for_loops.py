import random

num_cashiers = 1

num_cooks = 2

waiting_to_order = 0
waiting_for_food = 0

for minute in range(300):

# Customers arrive every minute and line up to order.
    waiting_to_order = waiting_to_order + random.randint(0, 6)
    

    # Each cashier can take up to three orders per minute.
    new_orders = min(num_cashiers * 3, waiting_to_order)
    done_orders = min(num_cooks, waiting_for_food)

    # After ordering, customers wait for their food to be made.
    waiting_to_order = waiting_to_order - new_orders
    waiting_for_food = waiting_for_food + new_orders
    waiting_for_food = waiting_for_food - done_orders
    

    
    

    print(str(waiting_to_order) + " customers waiting to order.")
    print(str(waiting_for_food) + " customers waiting for food.")