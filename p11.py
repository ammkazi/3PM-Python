# 789
# 7+8+9 = 24 (sum of digits)

n = int(input("Enter a num "))
rem = 0
sum = 0

while n!=0:
    rem = n%10
    sum = sum + rem
    n = n//10

print("Sum of digits is ", sum)


''''
n = 789
rem = 9
sum = 0 + 9 = 9

n = 78
rem = 8
sum = 9+ 8 = 17

n = 7
rem = 7
sum = 7 + 17 = 24

n = 0

'''