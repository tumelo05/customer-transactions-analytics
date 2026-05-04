import pandas as pd
import pyodbc

# --- SQL Server connection (WSL-safe) ---
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=127.0.0.1,1433;"
    "DATABASE=CustomerAnalytics;"
    "UID=bi_user;"
    "PWD=StrongPassword123!;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()
cursor.fast_executemany = True

# --- Load customers ---
customers = pd.read_csv("data/curated/customers_clean.csv")

customers["registration_datetime"] = pd.to_datetime(
    customers["registration_datetime"]
).dt.tz_localize(None)

customer_rows = customers[
    ["customer_id", "email", "name", "city", "state", "registration_datetime"]
].values.tolist()

cursor.executemany(
    """
    INSERT INTO dim_customers
    (customer_id, email, name, city, state, registration_datetime)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    customer_rows,
)

conn.commit()
print("Customers loaded")

# --- Load transactions ---
transactions = pd.read_csv("data/curated/transactions_clean.csv")

transactions["transaction_datetime"] = pd.to_datetime(
    transactions["transaction_datetime"]
).dt.tz_localize(None)

transaction_rows = transactions[
    ["transaction_id", "transaction_datetime", "customer_id",
     "product_id", "variation_id", "units"]
].values.tolist()

cursor.executemany(
    """
    INSERT INTO fact_transactions
    (transaction_id, transaction_datetime, customer_id,
     product_id, variation_id, units)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    transaction_rows,
)

conn.commit()
cursor.close()
conn.close()

print("Transactions loaded")
print(" Data successfully loaded into SQL Server")