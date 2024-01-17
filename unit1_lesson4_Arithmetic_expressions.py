base_price = input("Enter cart total: ")
user_float = float(base_price)

# Available coupon codes include 15% off and $12 off.
percent_discount = user_float- user_float * .15
fixed_discount = user_float - 12

# Pick the coupon that offers the best discount.
final_price = min(fixed_discount, percent_discount)
print("Your best price is $" + str (final_price))
