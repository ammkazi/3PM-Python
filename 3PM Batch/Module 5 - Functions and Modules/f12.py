def create_students(**details):
    print(f"{type(details)}")
    for key, value in details.items():
        print(f" {key:<10}: {value}")
    return details

create_students(name="Arkaan", age = 21, gender = "Male", Grade = "12th" )
