item_price = 50
customer_has_coupon = True


if customer_has_coupon == True:
    final_price = item_price * 0.9

else:
    final_price = item_price

print (f"Price: ${final_price}")