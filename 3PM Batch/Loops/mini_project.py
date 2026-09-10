account = {
    "name" : "Zeeshan",
    "account_no" : 12345,
    "balance" : 5000
}

while True:
    print("==== BANK ACCOUNT ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1: 
            print(f"\nCurrent Balance: ₹{account['balance']}")
        case 2:

            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                account['balance'] = account["balance"] + amount
                print("Deposit successful!")
                print(f"New balance ₹{account['balance']}")

            else:
                print("Invalid amount")

        case 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount!")
            elif amount > account["balance"]:
                print("insuffient balance")
            else:
                account["balance"] = account["balance"] - amount
                print("Withdraw Successful")
                print(f"Remaining balance: ₹{account['balance']}")
        case 4:
            print("==== Account Details ====")
            print(f"Name: {account['name']}")
            print(f"Account Number: {account['account_no']}")
            print(f"Balance: {account['balance']}")

        case 5:

            print("Thankyou for using our services!")
            break

        case _:
            print("\n Invalid choice. Please try again.")
