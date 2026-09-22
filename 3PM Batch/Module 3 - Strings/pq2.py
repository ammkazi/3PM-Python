for attempt in range(1, 4):

    password = input("Enter your password: ")

    if len(password) < 8:
        print("Weak Password")
        print("Password must contain at least 8 characters.")
        continue

    has_digit = False
    has_uppercase = False
    has_lowercase = False

    for char in password:

        if char.isdigit():
            has_digit = True

        elif char.isupper():
            has_uppercase = True

        elif char.islower():
            has_lowercase = True

    if has_digit and has_uppercase and has_lowercase:

        print("Strong Password")
        break

    else:
        print("Weak Password")