order_amount = int(input("enter order amount: "))
# if else ladder
if order_amount < 200:
    delivery_charge = 50
elif order_amount < 500:
    delivery_charge = 30
elif order_amount < 1000:
    delivery_charge = 10
else:
    delivery_charge = 0


final_amt = order_amount + delivery_charge
print("Delivery charge ₹", delivery_charge)
print("Final amount: ₹", final_amt)