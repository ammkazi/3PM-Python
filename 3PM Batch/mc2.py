print("===== FOOD MENU =====")
print("1. Burger -- ₹150")
print("2. Pizza -- ₹450")
print("3. Pasta -- ₹200")
print("4. Sandwich -- ₹150")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        item = "Burger"
        price = 150
        
    case 2:
        item = "Pizza"
        price = 450

    case 3:
        item = "Pasta"
        price = 200

    case 4:
        item = "Sandwich"
        price = 150
       
quantity = int(input("Enter quantity: "))
total = price * quantity

print("\n===== ORDER SUMMARY =====")
print("Item: ", item)
print("Price: " , price)
print("Quantity: ",quantity)
print("Total Amount: ₹",total)