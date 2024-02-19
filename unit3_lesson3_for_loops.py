import random

num_cashiers = 1

waiting_to_order = 0
waiting_for_food = 0

# Customers arrive every minute and line up to order.
waiting_to_order = waiting_to_order + random.randint(0, 6)

# Each cashier can take up to three orders per minute.
new_orders = min(num_cashiers * 3, waiting_to_order)

# After ordering, customers wait for their food to be made.
waiting_to_order = waiting_to_order - new_orders
waiting_for_food = waiting_for_food + new_orders

print(str(waiting_to_order) + " customers waiting to order.")
print(str(waiting_for_food) + " customers waiting for food.")