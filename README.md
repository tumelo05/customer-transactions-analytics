# Customer Transactions Analytics Dashboard

## Overview
This project is an end-to-end customer analytics solution that transforms raw customer and transaction data into interactive business insights using Python, SQL Server, and Power BI.

Raw data in CSV and JSON format is cleaned and validated using Python, loaded into a SQL Server analytics database using a star-schema design, and visualized through an interactive Power BI dashboard.

---

## Architecture
1. Raw customer and transaction data ingested from CSV and JSON files  
2. Data cleaned and transformed using Python (Pandas)
3. Structured data loaded into SQL Server with enforced primary and foreign key constraints
4. Analytics views created for validation and exploration
5. Power BI dashboard built on a dimensional model for reliable filtering and interactivity

---

## Technologies Used
- **Python**: Data cleaning and transformation
- **SQL Server**: Data modeling, constraints, and analytics views
- **Power BI**: Interactive dashboards and KPI reporting
- **Data Formats**: CSV, JSON

---

## Dashboard Features
- KPI cards for total customers, total transactions, and total units sold
- Daily transaction volume trend analysis
- Customer performance table with transaction counts and total units
- Top 10 customers by transaction volume
- Dynamic state-level filtering via slicers

---

## Dashboard Preview
![Dashboard Overview](images/dashboard_overview.png)

---

## How to Reproduce
1. Run SQL scripts in the `sql/` directory to create tables and views
2. Execute Python scripts in `python/` to clean and load data
3. Open the Power BI file located in `powerbi/customer_analytics_dashboard.pbix`

---

## Notes
SQL views are used for analytical validation and exploration, while Power BI visuals are built directly on dimension and fact tables to ensure proper filter propagation and a stable semantic model.