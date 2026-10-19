def add_print(a, b):
    print(a + b)

def add_return(a, b):
     return a + b

x = add_print(2, 3) # prints 5, returns None
y = add_return(2, 3) # prints nothing, returns 
print("x is", x)
print("y is", y)