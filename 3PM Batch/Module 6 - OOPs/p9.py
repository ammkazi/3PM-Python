balance = 10000

try:

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise ValueError("Insufficient balance")

    balance = balance - amount

except ValueError as e:

    print("Transaction Failed:", e)

else:

    print("Withdrawal successful!")
    print("Remaining Balance:", balance)

finally:

    print("Thank you for using our ATM")