def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter a number to print its table: "))
table(n)