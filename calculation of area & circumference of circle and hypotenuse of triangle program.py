import math

# circumference of circle

radius = float(input("Enter the radius of a circlea: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)} cm")



# area of circle

radius = float(input("Enter the radius of a circlea: "))

area =  math.pi * pow(radius, 2)

print(f"The area of the circle  is: {round(area, 2)} cm^2")


# Hypo of triangle

a = float(input("Enter side A: "))
b = float(input("Enter side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {round(c, 2)}")

