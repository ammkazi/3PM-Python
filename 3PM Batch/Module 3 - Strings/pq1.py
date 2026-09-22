while True:
    units = float(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units")

    elif units == 0:
        print("No electricity consumption")

    else:
        remaining = units
        bill = 150

        first = min(remaining, 100)
        bill += first * 3
        remaining -= first

        if remaining > 0:
            second = min(remaining, 100)
            bill += second * 5
            remaining -= second

        if remaining > 0:
            third = min(remaining, 200)
            bill += third * 7
            remaining -= third

        if remaining > 0:
            bill += remaining * 10

        print("Bill: Rs.", bill)

        if units > 1000:
            print("High Consumption Alert")

    again = input("Calculate another bill? (Y/N): ").upper()

    if again == "N":
        break