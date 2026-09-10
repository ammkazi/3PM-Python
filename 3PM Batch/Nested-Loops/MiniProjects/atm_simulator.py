balance = 5000

# Pin Set
pin = input("Enter a pin: ")
while True:
    if len(pin) == 4:
        print("Pin set successfully")
        pin = int(pin)
        break
    else:
        print("Oops set a 4 digit pin!!")
        pin = input("Create a pin: ")

# Mini Statement
transactions = []

# Login
print("====== WELCOME TO ATM ======")
attempt = 0
while attempt < 3:
    entered_pin = int(input("Enter your pin to login to account: "))
    if entered_pin == pin:
        print("Login successful!\n")
        break
    else:
        attempt+=1
        print("Wrong PIN!")
        print("Attempts Left:", 3 - attempt)
if attempt == 3:
    print("Account Blocked! Too many wrong attempts.")
    exit()

# ATM Menu
while True:

    print("\n====== ATM MENU ======")
    print("1. Balance Enquiry")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Mini Statement")
    print("6. Exit")

    choice = int(input("Select an option between 1 and 6: " ))

    match choice:
        case 1:
            print(f"\nCurrent Balance: ₹{balance}")

        case 2:
            amount = int(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Invalid amount !!")
            else:
                balance = balance + amount
                transactions.append("Deposited : ₹ " + str(amount))
                print("Deposit Successful!")
                print("Current Balance = ₹", balance)

        case 3:
            amount = int(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                    print("Invalid amount!")
            elif amount > 10000:
                print("Withdrawal limit is ₹10,000.")
            elif amount % 100 != 0:
                print("Amount must be a multiple of 100.")
            elif balance - amount < 500:
                print("Minimum balance of ₹500 must be maintained.")

            else:
                balance -= amount # balance = balance - amount
                transactions.append("Withdrawn ₹ : " + str(amount))

                print("Withdrawal Successful!")
                print("Please collect your cash.")
                print("Remaining Balance = ₹", balance)

        case 4:
            # Change PIN
            old_pin = input("Enter your current pin: ")
            if int(old_pin) == pin:
                new_pin = input("Enter a new pin: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    print("PIN changed succesfully!")
                    pin = new_pin
                else:
                    print("PIN must have 4 digits only")
            else:
                print("Incorrect current pin")

        case 5:
            print("\n====== MINI STATEMENT ======")
            if len(transactions) == 0:
                print("No successful transactions.")
            else:
                for i, transaction in enumerate(transactions, start=1):
                    print(i , "." , transaction)
                print("Current Balance = ₹", balance)
        case 6:
            print("\nThank you for using our ATM.")
            print("Please collect your card.")
            break
        case _:
            print("Invalid choice! Please enter 1 to 6.")