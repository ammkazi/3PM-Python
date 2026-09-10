#movie-ticket prcing
age = int(input("Enter your age: "))
ticket = int(input("Enter number of tickets: "))

if age < 5:
    ticket_price = 50
elif age < 18:
    ticket_price = 150
elif age < 45: 
    ticket_price = 300
elif age < 65:
    ticket_price = 400
else:
    ticket_price = 180

total_cost = ticket_price * ticket

print("price of one ticket: ", ticket_price)
print("Total ticket cost: ₹", total_cost)