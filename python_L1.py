# ==============================
# PYTHON BASICS – ALL IN ONE FILE
# ==============================

# 1. Printing Output
print("Hello, World!")

# 2. Variables & Data Types
x = 10
y = 3.5
name = "Haider"
is_active = True

print("x:", x)
print("y:", y)
print("name:", name)
print("is_active:", is_active)
print("Type of x:", type(x))

# 3. Taking Input
user_name = input("Enter your name: ")
print("Welcome,", user_name)

# 4. Operators
a = 10
b = 3
print("Addition:", a + b)
print("Division:", a / b)
print("Power:", a ** b)
print("Is a > b?", a > b)

# 5. Conditional Statements
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an Adult")
elif age >= 13:
    print("You are a Teenager")
else:
    print("You are a Child")

# 6. Loops
print("For loop:")
for i in range(1, 6):
    print(i)

print("While loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# 7. Data Structures

# List
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Fruits list:", fruits)

# Tuple
colors = ("red", "blue", "green")
print("Colors tuple:", colors)

# Set
numbers = {1, 2, 3, 3, 4}
print("Set (no duplicates):", numbers)

# Dictionary
student = {"name": "Ali", "age": 20}
print("Student name:", student["name"])

# 8. Functions
def add(a, b):
    return a + b

print("Sum from function:", add(5, 7))

# 9. File Handling
with open("sample.txt", "w") as file:
    file.write("This is a Python basics file.")

print("File written successfully.")

# 10. Exception Handling
try:
    num = int(input("Enter a number: "))
    print("Number entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

# 11. Importing Modules
import math
print("Square root of 16:", math.sqrt(16))

# 12. End of Program
print("Python basics completed successfully")
