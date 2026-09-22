available = 50

while True:

    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Check Available Spaces")
    print("4. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":

            if available == 0:
                print("Parking Full")
                print("Available spaces:", available)
                continue

            vehicle = input("Vehicle type (C=Car, B=Bike, T=Truck): ").upper()

            if vehicle == "C":
                rate = 40

            elif vehicle == "B":
                rate = 20

            elif vehicle == "T":
                rate = 70

            else:
                print("Invalid vehicle type")
                continue

            hours = float(input("Hours parked: "))

            if hours <= 0:
                print("Invalid hours")
                continue

            charge = rate * hours

            available -= 1

            print("Parking charge: Rs.", charge)

        case "2":

            if available < 50:
                available += 1
                print("Vehicle removed.")

            else:
                print("Parking is already empty.")

        case "3":

            print("Available spaces:", available)

        case "4":

            break

        case _:
            print("Invalid choice")

    print("Available spaces:", available)