number = int(input("Enter a number to calculate factorial: "))

factorial = 1

for i in range(1, number+1):
    factorial = factorial * i

print(f"Factorial of number {number} is {factorial}")