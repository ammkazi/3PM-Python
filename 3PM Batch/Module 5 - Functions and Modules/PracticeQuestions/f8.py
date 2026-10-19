# Write area_of_circle(radius) that prints the area to two decimals.
import math
def area_of_circle(radius):
    return round(math.pi * radius ** 2, 2)

radius = int(input("Enter radius to calculate the area of circle: "))
print(f"Area of circle for radius {radius} is : {area_of_circle(radius)}")