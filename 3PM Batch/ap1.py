print(" ==== ECOMMERCE APP ==== ")

print("\n Available Products:")
print("1. Keyboard         - ₹1500")
print("2. Mouse            - ₹2000")
print("3. Headphone        - ₹2500")
print("4. Webcam           - ₹3000")

choice = int(input("\nEnter your product choice: "))

match choice:

    case 1:
        product_name = "Keyboard"
        price = 1500
    case 2:
        product_name = "Mouse"
        price = 2000
    case 3:
        product_name = "Headphone"
        price = 3000
    case 4:
        product_name = "Webcam"
        price = 3000
    case _:
        print("Invalid option, Exiting program!")
        exit()

quantity = int(input("Enter quantity: "))
subtotal = price * quantity

print("\nCustomer Type: ")
print("1. Regular")
print("2. Student")

customer_type = int(input("Enter your choice: "))

student_discount = 0

if customer_type == 2:
    student_discount = subtotal * 0.05

coupon = input("\nEnter your coupon code: ")
coupon_discount = 0

if coupon == "SAVE10":
    coupon_discount = subtotal * 0.10
else:
    coupon_discount = 0

total_discount = student_discount + coupon_discount

if subtotal  > 2000:
    delivery_charge = 0
else:
    delivery_charge = 200

final_amount = subtotal - total_discount + delivery_charge


# Order Summary
print("\n ==== Order Summary ====: ")
print("Product Name: ", product_name)
print("Quantity: ", quantity)
print("Price: ", price)
print("Subtotal: ",subtotal)
print("Student Discount: ", student_discount)
print("Coupon Discount: ", coupon_discount)
print("Total Discount: ", total_discount)

if delivery_charge == 0:
    print("Delivery:    FREE")
else:
    print("Delivery:    ₹",delivery_charge)

print("------------------------------------------")
print("Final Amount:        ₹",final_amount)
print("------------------------------------------")
print("\nOrder Confirmed")
