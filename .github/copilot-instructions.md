# Copilot / AI Agent Instructions

> Purpose: give AI coding agents just enough, focused context to be immediately productive in this repository. Keep it short and concrete — no generic advice.

##  High-level summary
- This repository contains progressive learning examples for Python and PySpark, from basics (L1) to advanced data engineering concepts (L3).
- Primary languages: **Python** (+ PySpark). Primary runtime: **Python interpreter** for basic scripts, **Apache Spark** (local) for PySpark examples.

##  How to run locally (expected commands)
- Run Python examples:
  ```bash
  python python_L1.py
  ```
- Run PySpark examples (requires PySpark and Java installed):
  ```bash
  python pyspark_L1.py
  ```
- No build, test, or packaging commands present.

##  Project layout notes (where to look and what matters)
- Source code: all example scripts are in the root directory, named `python_LX.py` for Python concepts and `pyspark_LX.py` for PySpark examples (X = level).
- Data files: `data.json` and `sample.txt` provide sample data for examples.
- Libraries reference: `python_libraries.py` demonstrates common Python libraries with fallbacks.
- No dedicated tests, config, or build directories.

##  Common patterns to follow in this repo
- Standalone scripts without CLI arguments or external configuration.
- For PySpark scripts, initialize `SparkSession` explicitly with `SparkSession.builder.appName(...).getOrCreate()` and call `spark.stop()` at the end.
- Progress from basic syntax in L1 to advanced features like logging, type hints, and generators in L3.
- Use `logging` module instead of `print` for output in advanced examples.
- Implement library fallbacks with try-except blocks when demonstrating optional dependencies, as in `python_libraries.py`.
- Use `if __name__ == "__main__":` guard for main execution in production-style scripts.

##  PR guidance for Copilot / AI agents
- As a learning repository, contributions typically add new examples or expand existing levels.
- Follow naming conventions: `python_LX.py` or `pyspark_LX.py` for new levels.
- Include comments explaining concepts, as seen in `python_L3.py`.

##  Debugging tips specific to this project (if present)
- For PySpark scripts, ensure Java is installed and `JAVA_HOME` is set; install PySpark via `pip install pyspark`.
- Check console output or `app.log` (created by logging in L3) for errors.
- Examples are designed for local execution; no cluster setup required.

##  Files & patterns to reference when updating these instructions
- `pyspark_L1.py` for basic Spark session and DataFrame creation.
- `python_L3.py` for advanced patterns like logging and type hints.
- `python_libraries.py` for library usage and fallback implementations.
