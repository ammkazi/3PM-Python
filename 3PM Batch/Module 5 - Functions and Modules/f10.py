# Write bmi(weight, height) that prints the value and the category

def bmi(weight, height):
    height = height / 100
    value = weight // (height**2)
    print("BMI:", round(value, 2))
    if value < 18.5:
        print("Category: Underweight")
    elif value < 25:
        print("Category: Normal weight")
    elif value < 30:
        print("Category: Overweight")
    else:
        print("Category: Obesity")

w = int(input("Enter your weight: "))
h = float(input("Enter your height: "))

bmi(w,h)