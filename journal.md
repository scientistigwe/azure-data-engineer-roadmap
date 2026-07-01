# Azure Data Engineer Job-Ready Learning Journal

> Last updated: 1 July 2026

---

## Day 1 — Python ETL basics

**Phase:** Foundation

### What I Did

1. I designed and implemented a Python ETL pipeline.
2. The etl.py features include: Automatic file discovery, Encoding and delimiter detection (with fallback support), Preservation of original filenames in the output (`<filename>_processed.csv`), Logging, and resilient error handling.
3. Ref Question 1: Environment-induced missing rows (Order-dependent ETL Logic): glob.glob() does not guarantee the order in which files are returned. As a result, different environments (e.g., your local machine and a CI server) may process the same files in different sequences, leading to inconsistent ETL results if the processing is order-dependent. The fix is to make the file order deterministic by sorting the file list before processing. Example: `files = sorted(glob.glob("data/**/*.csv", recursive=True))`
4. In etl.py, I used return `sorted(self.source_folder.rglob("*.csv"))`. `pathlib.Path.rglob()` provides a more modern, object-oriented approach to file discovery than `glob.glob()`. Wrapping it with `sorted()` also ensures deterministic file processing, preventing environment-specific differences in file ordering between local and CI environments.

### To Explore Further



---
