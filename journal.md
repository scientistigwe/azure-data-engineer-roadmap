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
5. Ref Question 2: ETL Logging Best Practices: The minimum logging for a production ETL should capture five key events: ETL start, file extraction, transformation summary, load completion, and ETL completion or failure. Each log should include enough contextual information—such as filenames, row counts, encoding and delimiter (where applicable), rows processed, destination, execution time, and any exception details—to enable monitoring, troubleshooting, and auditing of the pipeline without overwhelming the logs.
6. Ref Question 3: Why Split ETL into Extract, Transform, and Load Functions: Splitting ETL into `extract`, `transform`, and `load` functions makes the pipeline easier to understand, test, debug, and maintain. In a monolithic script, if the job fails halfway through, it can be difficult to tell whether the problem came from reading the source file, applying transformation logic, or writing the output.  For example, if a CSV file has the wrong delimiter, a monolithic script may fail later during transformation with a confusing column error. By separating the ETL stages, the issue is isolated in the `extract` function, where delimiter detection and file-reading logic belong. This prevents the error from being mistaken for a transformation problem and makes the fix easier to apply without changing the rest of the pipeline.  The three-function approach also allows each stage to be reused, tested independently, and logged clearly, making the ETL process more reliable and easier to support in production.

### To Explore Further



---
