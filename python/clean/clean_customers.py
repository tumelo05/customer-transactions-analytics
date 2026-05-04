import pandas as pd
import json

# Load raw customers
df = pd.read_csv("data/raw/customers.csv")

# Drop rows with no customer_id
df = df[df["customer_id"].notna()]

# Drop rows with both name and email missing
df = df[~(df["name"].isna() & df["email"].isna())]

# Normalize email
df["email"] = df["email"].str.lower().str.strip()

# Parse address JSON safely
def parse_address(addr):
    if pd.isna(addr):
        return pd.Series({"city": None, "state": None})
    try:
        obj = json.loads(addr)
        return pd.Series({
            "city": obj.get("city"),
            "state": obj.get("state")
        })
    except Exception:
        return pd.Series({"city": None, "state": None})

address_parsed = df["address"].apply(parse_address)
df = pd.concat([df, address_parsed], axis=1)

# Combine date + timezone → UTC
df["registration_datetime"] = pd.to_datetime(
    df["registration_date"] + df["registration_date_tz"],
    errors="coerce",
    utc=True
)

# Select curated columns
customers_clean = df[[
    "customer_id",
    "email",
    "name",
    "city",
    "state",
    "registration_datetime"
]]

# Save curated output
customers_clean.to_csv(
    "data/curated/customers_clean.csv",
    index=False
)

print(f"Cleaned customers rows: {len(customers_clean)}")
