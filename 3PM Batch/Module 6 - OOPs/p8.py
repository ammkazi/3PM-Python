try:

    num = int(input("Enter a number: "))

    result = 100 / num

except ValueError:

    print("Please enter a valid integer")

except ZeroDivisionError:

    print("Number cannot be zero")

else:

    print("Result:", result)

finally:

    print("Thank you for using the program")