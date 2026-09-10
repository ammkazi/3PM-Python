original = int(input("Enter a positive number: "))
number = original

digit_count = 0
digit_sum = 0
reversed_num = 0

while number > 0:
    digit = number % 10
    number = number // 10
    digit_sum += digit
    digit_count+=1
    reversed_num = reversed_num * 10 + digit