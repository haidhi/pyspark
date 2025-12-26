# ======================================
# PYTHON LEVEL 2 – INTERMEDIATE CONCEPTS
# ======================================

# 1. Functions with default & keyword arguments
def greet(name, city="Unknown"):
    return f"Hello {name} from {city}"

print(greet("Haider"))
print(greet("Haider", city="Delhi"))

# 2. *args and **kwargs
def calculate_total(*numbers):
    return sum(numbers)

print("Total:", calculate_total(10, 20, 30))

def print_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_details(name="Ali", age=22, course="Python")

# 3. Lambda functions
square = lambda x: x * x
print("Square:", square(5))

# 4. map(), filter(), reduce()
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
even_nums = list(filter(lambda x: x % 2 == 0, numbers))

from functools import reduce
total = reduce(lambda a, b: a + b, numbers)

print("Squared:", squared)
print("Even numbers:", even_nums)
print("Total:", total)

# 5. List Comprehension
cubes = [x**3 for x in numbers if x % 2 != 0]
print("Cubes of odd numbers:", cubes)

# 6. Dictionary Comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Squares dict:", squares_dict)

# 7. Working with Strings
text = "python programming"
print(text.upper())
print(text.title())
print(text.replace("python", "Python"))

# 8. Date & Time
from datetime import datetime
now = datetime.now()
print("Current date & time:", now)

# 9. Reading Files
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# 10. Object-Oriented Programming (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Haider", 21)
print(person1.introduce())

# 11. Inheritance
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def details(self):
        return f"{self.name} studies {self.course}"

student1 = Student("Ali", 22, "Python")
print(student1.details())

# 12. Custom Exception
class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Age must be 18 or above")
    print("Age accepted")
except AgeError as e:
    print("Error:", e)

print("Level 2 Python completed 🎯")
