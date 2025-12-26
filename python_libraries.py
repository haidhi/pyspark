# =====================================================
# MOST USED PYTHON LIBRARIES – ALL IN ONE SCRIPT
# =====================================================

# MOST IMPORTANT LIBRARIES BY ROLE
# 🔹 Data Engineer

# Pandas

# NumPy

# PySpark

# SQLAlchemy

# Requests

# Logging

# 🔹 Backend Developer

# FastAPI / Flask

# Requests

# SQLAlchemy

# Pydantic

# 🔹 Data Scientist

# NumPy

# Pandas

# Matplotlib

# Scikit-learn

# 1. NumPy – Numerical Computing
try:
    import numpy as np
except Exception:
    # Minimal fallback for environments without numpy:
    class SimpleArray(list):
        def __pow__(self, other):
            return SimpleArray([x ** other for x in self])

    class _NumpyFallback:
        def array(self, seq):
            return SimpleArray(seq)

        def mean(self, arr):
            return sum(arr) / len(arr)

    np = _NumpyFallback()

arr = np.array([1, 2, 3, 4])
print("NumPy Array:", arr)
print("Mean:", np.mean(arr))
print("Squared:", arr ** 2)

print("-" * 40)

# 2. Pandas – Data Analysis
try:
    import pandas as pd
except Exception:
    # Minimal fallback for environments without pandas:
    class Column(list):
        def __ge__(self, other):
            return [x >= other for x in self]
        def __le__(self, other):
            return [x <= other for x in self]
        def __gt__(self, other):
            return [x > other for x in self]
        def __lt__(self, other):
            return [x < other for x in self]
        def __eq__(self, other):
            return [x == other for x in self]

    class SimpleDataFrame:
        def __init__(self, data):
            self.columns = list(data.keys())
            length = len(next(iter(data.values()))) if data else 0
            self.rows = [
                {k: data[k][i] for k in self.columns}
                for i in range(length)
            ]

        def __repr__(self):
            # show a simple table-like representation
            header = " | ".join(self.columns)
            lines = [" | ".join(str(row[c]) for c in self.columns) for row in self.rows]
            return header + ("\n" + "\n".join(lines) if lines else "")

        def __str__(self):
            return self.__repr__()

        def __getitem__(self, key):
            if isinstance(key, str):
                return Column([row[key] for row in self.rows])
            if isinstance(key, list):
                filtered = [row for row, keep in zip(self.rows, key) if keep]
                return SimpleDataFrame({k: [r[k] for r in filtered] for k in self.columns})
            raise KeyError(key)

    class _PandasFallback:
        DataFrame = SimpleDataFrame

    pd = _PandasFallback()

data = {
    "name": ["Ali", "Sara", "John"],
    "age": [22, 18, 30]
}

df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)

adults = df[df["age"] >= 18]
print("Adults:")
print(adults)

print("-" * 40)

# 3. Matplotlib – Visualization
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 4. Requests – API Calls
import requests

response = requests.get("https://api.github.com")
print("API Status Code:", response.status_code)

print("-" * 40)

# 5. JSON – Data Exchange
import json

json_data = {
    "name": "Haider",
    "role": "Engineer",
    "skills": ["Python", "PySpark"]
}

json_string = json.dumps(json_data)
print("JSON String:", json_string)

loaded_json = json.loads(json_string)
print("Loaded Name:", loaded_json["name"])

print("-" * 40)

# 6. OS & SYS – System Info
import os
import sys

print("Current Directory:", os.getcwd())
print("Python Version:", sys.version)

print("-" * 40)

# 7. Datetime – Date & Time
from datetime import datetime

now = datetime.now()
print("Current Date & Time:", now)

print("-" * 40)

# 8. Logging – Production Logging
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.warning("This is a warning message")

print("-" * 40)

# 9. SQLite (SQL Basics) – Database
import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Ali", 22))
conn.commit()

cursor.execute("SELECT * FROM users")
print("Database Rows:", cursor.fetchall())

conn.close()

print("-" * 40)

# 10. PySpark – Big Data (Requires Spark Installed)
try:
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("Demo").getOrCreate()

    spark_data = [("Ali", 22), ("Sara", 18)]
    spark_df = spark.createDataFrame(spark_data, ["name", "age"])

    print("PySpark DataFrame:")
    spark_df.filter(spark_df.age >= 18).show()

    spark.stop()

except Exception as e:
    print("PySpark not configured:", e)

print("-" * 40)

# 11. SQLAlchemy – ORM
try:
    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///example.db")
    conn = engine.connect()

    result = conn.execute("SELECT * FROM users")
    print("SQLAlchemy Result:", result.fetchall())

    conn.close()

except Exception as e:
    print("SQLAlchemy error:", e)

print("-" * 40)

# 12. pytest-style Test Example
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

print("Test add():", add(2, 3))

print("-" * 40)

print("All major Python libraries demo completed 🚀")
