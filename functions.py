
def rectangle_area(length, width):
    return length * width


import math
def circle_area(radius):
    return math.pi * radius ** 2


def triangle_area(base, height):
    return 0.5 * base * height


def main():
    print("Welcome to the Shape Area Calculator!")

    
    print("Rectangle Area:", rectangle_area(5, 10))

    
    print("Circle Area:", circle_area(7))

 
    print("Triangle Area:", triangle_area(6, 8))


main()

# Functions to perform operations

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

# Use the functions
num1 = 5
num2 = 7

print("Sum:", add(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num2, num1)) 
print("Subtraction:", subtract(num2, num1))
