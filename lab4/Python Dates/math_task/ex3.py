import math

n = int(input("Input number of sides:"))

s = int(input("Input the length of a side:"))

area = math.ceil((n * (s*s))/4*math.tan(math.pi/n))


print("The area of the polygon is:",area)