try:

    a = 10
    b = 5

    result = a / b

except ZeroDivisionError:

    print("Cannot divide by zero")

else:

    print("Division successful")
    print("Result:", result)