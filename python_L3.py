# =====================================================
# PYTHON LEVEL 3 – DATA ENGINEERING & ADVANCED CONCEPTS
# =====================================================

# 1. Virtual Environment & Dependency Concept (INFO)
# Use:
# python -m venv venv
# source venv/bin/activate (Linux/Mac)
# venv\Scripts\activate (Windows)

# 2. Logging (Industry standard – replaces print)
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")

# 3. Type Hinting (important for clean code & teams)
def multiply(a: int, b: int) -> int:
    return a * b

result = multiply(4, 5)
logging.info(f"Multiply result: {result}")

# 4. Decorators (used in frameworks & pipelines)
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello from decorator")

say_hello()

# 5. Generators (memory-efficient – BIG DATA friendly)
def number_generator(n):
    for i in range(n):
        yield i

for num in number_generator(5):
    print("Generated:", num)

# 6. Context Managers (used in file/db handling)
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager("context.txt") as f:
    f.write("Using context manager")

# 7. Working with JSON (APIs / Config files)
import json

data = {
    "name": "Haider",
    "role": "Data Engineer",
    "skills": ["Python", "PySpark", "SQL"]
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("JSON Loaded:", loaded_data)

# 8. Multithreading (I/O bound tasks)
import threading
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} completed")

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

# 9. Multiprocessing (CPU bound tasks)
from multiprocessing import Process

def cpu_task():
    print("CPU intensive task running")

p = Process(target=cpu_task)
p.start()
p.join()

# 10. Python + SQL (very important for Data Engineers)
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
)
""")

cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ("Ali", 50000))
conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Employees:", rows)

conn.close()

# 11. PySpark-like Data Processing (LOGIC STYLE)
data = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 17},
    {"name": "John", "age": 30}
]

# filter + map style
adults = list(filter(lambda x: x["age"] >= 18, data))
names = list(map(lambda x: x["name"], adults))

print("Adult Names:", names)

# 12. Production-level main guard
def main():
    logging.info("Main pipeline executed")
    print("Pipeline completed successfully")

if __name__ == "__main__":
    main()

logging.info("Application finished")
