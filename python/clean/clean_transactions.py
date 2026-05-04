import pandas as pd
import json
import re

# Load raw JSON lines
with open("data/raw/transactions.json") as f:
    records = [json.loads(line) for line in f]

df = pd.DataFrame(records)

# --- CLEAN TRANSACTION DATE ---
# Remove text inside parentheses: "(Greenwich Mean Time)", "(British Summer Time)"
df["transaction_date"] = df["transaction_date"].str.replace(
    r"\s*\(.*\)$", "", regex=True
)

# Parse cleaned datetime string
df["transaction_datetime"] = pd.to_datetime(
    df["transaction_date"],
    utc=True,
    errors="coerce"
)

# Drop rows where parsing failed
df = df[df["transaction_datetime"].notna()]

# Convert UTC → naive datetime (SQL Server DATETIME2)
df["transaction_datetime"] = df["transaction_datetime"].dt.tz_convert(None)

# --- CLEAN UNITS ---
df["units"] = pd.to_numeric(df["units"], errors="coerce")
df = df[df["units"].notna()]

# --- SELECT CURATED COLUMNS ---
transactions_clean = df[
    [
        "transaction_id",
        "transaction_datetime",
        "customer_id",
        "product_id",
        "variation_id",
        "units",
    ]
]

# Save curated dataset
transactions_clean.to_csv(
    "data/curated/transactions_clean.csv",
    index=False
)

print(" transactions_clean.csv regenerated with valid datetimes")