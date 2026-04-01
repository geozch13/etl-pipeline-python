# Simple ETL Pipeline

A simple ETL pipeline in Python that fetches posts from a public API and
stores them in a SQLite database.

## Pipeline Steps

-   **Extract** → Fetch data from a public API
-   **Transform** → Filter required fields (`userId`, `id`, `title`)
-   **Load** → Insert data into a SQLite database

## How to Run

``` bash
python run_pipeline.py 10
```

-   `10` = number of records per batch
-   If no argument is provided, the default batch size from `config.py`
    is used

## Features

-   Incremental loading (fetches new data based on last inserted ID)
-   Idempotent inserts (no duplicate records)
-   Configurable batch size (via config or CLI)
-   Basic error handling (API and DB failures)
-   Simple logging with clear execution steps

## Project Structure

    extract.py        # Extract & transform step
    load_db.py        # Load into SQLite
    config.py         # Configuration variables
    run_pipeline.py   # Pipeline entry point

## Use Case

This project simulates a real-world ETL pipeline where data is: 
- extracted from an API
- validated and cleaned
- stored for analytical use

## Requirements

``` bash
pip install -r requirements.txt
```
