approved = 0
further_verification = 0
rejected = 0

for customer in range(1, 6):

    print("\nCustomer", customer)

    age = int(input("Enter age: "))

    if age < 18:
        print("Not Eligible")
        continue

    salary = float(input("Enter monthly salary: "))

    credit_score = int(input("Enter credit score: "))

    existing_loan = input("Existing loan? (Y/N): ").upper()

    if (21 <= age <= 60 and
        salary >= 30000 and
        credit_score >= 700 and
        existing_loan == "N"):

        print("Loan Approved")
        approved += 1

    elif salary >= 30000 and 650 <= credit_score < 700:

        print("Further Verification")
        further_verification += 1

    else:

        print("Loan Rejected")
        rejected += 1

print("\n--- Final Results ---")
print("Approved:", approved)
print("Further Verification:", further_verification)
print("Rejected:", rejected)