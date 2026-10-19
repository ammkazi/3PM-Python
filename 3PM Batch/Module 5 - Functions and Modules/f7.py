def userLogin(name, password):
    if name == "Zeeshan" and password == "abc123":
        return "Login Successfully"
    else:
        return "Login failed."

def display(status):
    print(status)


uname = input("Enter username: ")
password = input("Enter password: ")

result = userLogin(uname, password)

display(result)