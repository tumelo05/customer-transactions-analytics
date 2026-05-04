
USE CustomerAnalytics;
GO

USE CustomerAnalytics;
GO

-- 1. Transactions per customer
CREATE OR ALTER VIEW vw_transactions_per_customer AS
SELECT
    c.customer_id,
    c.name,
    c.state,
    COUNT(t.transaction_id) AS transaction_count,
    SUM(t.units) AS total_units
FROM dim_customers c
LEFT JOIN fact_transactions t
    ON c.customer_id = t.customer_id
GROUP BY
    c.customer_id,
    c.name,
    c.state;
GO

-- 2. Daily transaction trends
CREATE OR ALTER VIEW vw_daily_transactions AS
SELECT
    CAST(transaction_datetime AS DATE) AS transaction_date,
    COUNT(*) AS transaction_count,
    SUM(units) AS total_units
FROM fact_transactions
GROUP BY CAST(transaction_datetime AS DATE);
GO

-- 3. State-level customer activity
CREATE OR ALTER VIEW vw_state_customer_activity AS
SELECT
    c.state,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    COUNT(t.transaction_id) AS transaction_count,
    SUM(t.units) AS total_units
FROM dim_customers c
LEFT JOIN fact_transactions t
    ON c.customer_id = t.customer_id
GROUP BY c.state;
GO

SELECT TOP 5 * FROM vw_transactions_per_customer;
SELECT TOP 5 * FROM vw_daily_transactions;
SELECT TOP 5 * FROM vw_state_customer_activity;
