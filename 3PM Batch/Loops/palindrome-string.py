string = input("Enter a string to check palindrome: ")
string = string.replace(" ", "").lower()

if string == string[::-1]:
    print("Given string is a palindrome.")
else:
    print("Given string is not a palindrome.")