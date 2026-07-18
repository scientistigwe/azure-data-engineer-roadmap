# Senior Azure Data Engineer Job-Ready Learning Journal

> Last updated: 18 July 2026

## Summary

- Track: Senior Azure Data Engineer Job-Ready
- Weeks with evidence: 2
- Lesson entries captured: 3

| Week | Evidence entries | Completed | Last updated |
| --- | ---: | ---: | --- |
| [Week 1: Seed days: Setup](#week-1-seed-days-setup) | 1 | 1 | 30 Jun 2026, 19:24 |
| [Week 2: Seed days: Foundation](#week-2-seed-days-foundation) | 2 | 1 | 18 Jul 2026, 12:26 |

---

## Week 1: Seed days: Setup

### Lesson 1: Set up your Azure data engineering portfolio

| Field | Value |
| --- | --- |
| Lesson slug | `az-seed-day-01` |
| Phase | Setup |
| Saved/updated | 30 Jun 2026, 19:24 |
| Completed tasks | 7 |
| Lesson complete | Yes |

---

## Week 2: Seed days: Foundation

### Lesson 1: Python ETL basics

| Field | Value |
| --- | --- |
| Lesson slug | `az-seed-day-02` |
| Phase | Foundation |
| Saved/updated | 04 Jul 2026, 10:01 |
| Completed tasks | 4 |
| Lesson complete | Yes |

### What I Did

- **Built:** I designed and implemented a Python ETL pipeline.
- **Verified:** The etl.py features include: Automatic file discovery, Encoding and delimiter detection (with fallback support), Preservation of original filenames in the output (`<filename>_processed.csv`), Logging, and resilient error handling.
- **Explained:** Ref Question 1: Environment-induced missing rows (Order-dependent ETL Logic): glob.glob() does not guarantee the order in which files are returned. As a result, different environments (e.g., your local machine and a CI server) may process the same files in different sequences, leading to inconsistent ETL results if the processing is order-dependent. The fix is to make the file order deterministic by sorting the file list before processing. Example: `files = sorted(glob.glob("data/**/*.csv", recursive=True))`
- **Applied:** In etl.py, I used return `sorted(self.source_folder.rglob("*.csv"))`. `pathlib.Path.rglob()` provides a more modern, object-oriented approach to file discovery than `glob.glob()`. Wrapping it with `sorted()` also ensures deterministic file processing, preventing environment-specific differences in file ordering between local and CI environments.
- **Applied:** Ref Question 2: ETL Logging Best Practices: The minimum logging for a production ETL should capture five key events: ETL start, file extraction, transformation summary, load completion, and ETL completion or failure. Each log should include enough contextual information—such as filenames, row counts, encoding and delimiter (where applicable), rows processed, destination, execution time, and any exception details—to enable monitoring, troubleshooting, and auditing of the pipeline without overwhelming the logs.
- **Explained:** Ref Question 3: Why Split ETL into Extract, Transform, and Load Functions: Splitting ETL into `extract`, `transform`, and `load` functions makes the pipeline easier to understand, test, debug, and maintain. In a monolithic script, if the job fails halfway through, it can be difficult to tell whether the problem came from reading the source file, applying transformation logic, or writing the output.  For example, if a CSV file has the wrong delimiter, a monolithic script may fail later during transformation with a confusing column error. By separating the ETL stages, the issue is isolated in the `extract` function, where delimiter detection and file-reading logic belong. This prevents the error from being mistaken for a transformation problem and makes the fix easier to apply without changing the rest of the pipeline.  The three-function approach also allows each stage to be reused, tested independently, and logged clearly, making the ETL process more reliable and easier to support in production.
- **Applied:** I used SOLVE and 5-HOW approach to gain deeper  understanding of the case scenario and slice/dice questions.

### To Explore Further



### My Practice Work

---
<!-- framework:solve -->

## Python ETL basics
**Completed:** 2026-07-02 | **Method:** SOLVE

> **Scenario:** Scenario: RetailEdge Ltd receives daily POS export files from 15 UK store locations in CSV format. An analyst currently spends 90 minutes each morning manually merging and cleaning them. A repeatable Python ETL script will automate ingestion, validate row counts, log failures, and write clean output — reducing that to under a minute.

### S — Split the problem
- Input: Daily POS export files from 15 UK store locations.
Problem: The organisation currently spends valuable analytical time in manual ETL (data preparation) process.
Operation: A clean script that will automate ingestion, validate, log and handle error.
Product: A cleansed dataset saved in the output folder.
Success: A repeatable ETL run which finishes in under a minute.

- Input phrase: RetailEdge Ltd receives daily POS export files from 15 UK store locations in CSV format.
Process phrase: An analyst currently spends 90 minutes each morning manually merging and cleaning them.
Expected output: A repeatable Python ETL script will automate ingestion, validate row counts, log failures, and write clean output

- 1. Write a script that will do the following:
- loop through a directory and ingest 15 csv files (`file = pathlib.rglob(file_path, '/**/*.csv'`)
- read it in as DataFrame - `df = pd.read_csv(file)`
- log validations (rows in, rows out, rows dropped)
- Transform/cleanse the files (e.g. missing value, duplicates etc)
- Output the cleansed data into the destination

### O — Observe the data
- Raw dataset in csv format from 15 different store locations

- A python script to automate csv file ingestion, validation, transformation, logging and error handling.

- 1. Inconsistent delimiter
2. Schema drift
3. missing files
4. other data quality issues like duplicates, missingness, outliers etc

### V — Verify your logic
```python
Repo reference: foundation/src/etl.py
```

### E — Evolve the solution
- Add a validation checks and make the error handling more robust

- the evidence is in this repo ref path: `screenshots\foundation\python_etl_basics.png`

- I will commit the actual working code, take screenshot of the output print and explain what the methods in the ETLProcessor Object is doing

---

### Lesson 2: SQL joins, windows, and warehouse thinking

| Field | Value |
| --- | --- |
| Lesson slug | `az-seed-day-03` |
| Phase | Foundation |
| Saved/updated | 18 Jul 2026, 12:26 |
| Completed tasks | 0 |
| Lesson complete | In progress |

### What I Did

- **Note:** I learnt that grain of a table is the smallest meaningful unit of a table. Technically, its the identifier column which owns the table (primary key).
- **Applied:** CTEs - Common Text Expression is used to

### To Explore Further



### My Practice Work

---
<!-- framework:solve -->

## SQL joins, windows, and warehouse thinking
**Completed:** 2026-07-04 | **Method:** SOLVE

> **Scenario:** Scenario: RetailEdge's analytics team needs a weekly revenue report by product category and store region. Five analysts each write their own joins against the same raw tables and get five different totals. A shared dimensional model — one fact table, clear dimension tables, and standard window-function queries — will make every analyst's results agree.

### S — Split the problem
- Input: 
- Raw sales tables

Problem/Pain Point: 
- analyst write different join query
- each get different result

Operation:
- Create a shared dimensional model
- One fact table
- Clear dimension tables
- Standard window-function queries

Product: A shared dimensional model)
Success: Every analyst's results agree

---
