# Copilot / AI Agent Instructions — Starter

> Purpose: give AI coding agents just enough, focused context to be immediately productive in this repository. Keep it short and concrete — no generic advice.

## ✅ High-level summary
- This repository implements PySpark data processing jobs and related tooling (expected). If this is incorrect, update this section with the actual project purpose.
- Primary languages: **Python** (+ PySpark). Primary runtime: **Spark** (local / cluster via spark-submit).

## 🔧 How to run locally (expected commands)
- Run a Spark job locally (example):
  ```bash
  ./bin/spark-submit --master local[4] --py-files dist/package.zip src/main.py arg1 arg2
  ```
- Run tests (expected):
  ```bash
  pip install -r requirements.txt
  pytest -q
  ```
- Build packaging (if present):
  ```bash
  python -m build    # or setup.py sdist bdist_wheel
  ```

> If your repository uses Docker, Airflow, or a different test runner, replace the examples above with the commands found in the repo (e.g., `docker-compose up`, `airflow dags test`, `tox`).

## 🧭 Project layout notes (where to look and what matters)
- Source code: look for `src/`, `package_name/`, or `jobs/` for primary Spark job entrypoints (files like `main.py`, `job_*.py`).
- Tests: look for `tests/` or `integration_tests/`. Prefer using `pytest` flags such as `-k` to run a subset.
- Config: check for `conf/`, `config/*.yaml` or environment variables (.env). Treat config as authoritative.
- Jobs and submission: check for `scripts/` or `bin/` wrappers that call `spark-submit` — prefer using existing wrappers.

## 🧩 Common patterns to follow in this repo
- Prefer explicit Spark/session configuration via `SparkSession.builder.appName(...).config(...)` (avoid implicit global side effects).
- Jobs should accept CLI args and/or a config file; prefer `argparse` or `click` for consistent parsing.
- I/O should use stable storage paths (S3/HDFS) or `data/` for local testing. When creating temporary files, use `tmp/` or the system temp directory.

## ✅ PR guidance for Copilot / AI agents
- Limit changes to a single logical concern per PR.
- When adding or changing a job, include a minimal end-to-end test (pytest) that runs a small dataset locally with `local[*]` Spark master.
- Mention any runtime assumptions (Spark version, Python version) in the PR description.

## 🔍 Debugging tips specific to this project (if present)
- Reproduce locally with a small sample file in `tests/fixtures/` and run the job with `--master local[2]`.
- Check Spark logs (stderr/stdout) for executor and driver stack traces. Use `--conf spark.executor.memory=1g` to constrain resource usage when debugging locally.

## 📁 Files & patterns to reference when updating these instructions
- Add concrete examples from these files if they exist: `README.md`, `scripts/run_job.sh`, `bin/spark-submit`, `tests/test_*.py`, `conf/*.yaml`, `Dockerfile`, `.github/workflows/*`.

## 📝 When merging this file
- If a `.github/copilot-instructions.md` already exists, preserve any repository-specific examples and run commands; append missing sections from this file and call that out in the PR.

---

If you want, point me to any key files (entrypoints, CI, or config) and I will update these instructions with concrete examples (commands, file paths, and tests) so agents can operate with no hand-holding.