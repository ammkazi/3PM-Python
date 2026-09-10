number = int(input("Enter a number to check palindrome: "))

original = number

reverse = 0

while number > 0:
    digit = number % 10
    number = number // 10
    reverse = reverse * 10 + digit

if original == reverse:
    print("It is a palindrome number")

else:
    print("Not a palindrome")