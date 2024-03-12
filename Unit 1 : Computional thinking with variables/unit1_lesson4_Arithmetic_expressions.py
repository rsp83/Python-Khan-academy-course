base_price = input("Enter cart total: ")
float_base = float(base_price)
shipping_price = input("Enter shipping total: ")
float_shipping = float(shipping_price)

# Available coupon codes include 15% off and $12 off.
percent_discount = float_base- float_base * .15
fixed_discount = float_base - 12

# Pick the coupon that offers the best discount.
final_price = min(fixed_discount, percent_discount)
final_price_with_shipping = final_price + float_shipping
rounded_final_price = round(final_price_with_shipping, 2)
print("Your best price is $" + str (rounded_final_price))
