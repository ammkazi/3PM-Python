# #Operators


# # Arithmetic operators
# '''
# + => Add
# - => Subtract
# * => Multiply
# / => Division (quotient)
# % (Modulus)=> Remainder
# ** => Exponent 
# '''
# #Arithmetic operators
a = 10
b = 5

result = a + b
print(result)

result = a - b
print(result)

result = a * b
print(result)

result = a / b
print(result)

result = a % b
print(result)

result = 2 ** 4
print(result)

print(10//3)

# #Relational or Comparison Operators

# '''
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# != : Not equal to
# == : Equal to operator
# '''

print(5<3)

print(a==b)
print(a!=b)


# # Logical operators
# '''
# and operatop
# or operator
# not operator
# '''

x = 15
y = 20
# a = 10 , b = 5
print( (a>b) and (a!=b) )
print( (a>b) or (a<=b) )
print(not(a>b))

print(6>=5)

# Membership Operators
'''
in => checks if a value is present
not in => checks if a value is not present
'''


name = "Sahil"
print("S" not in name)
print("Z" not in name)

# Identity operators
a = 10
b = 10
print(a is not b)