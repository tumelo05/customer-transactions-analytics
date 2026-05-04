USE CustomerAnalytics;
GO

-- Dimension: Customers
CREATE TABLE dim_customers (
    customer_id UNIQUEIDENTIFIER NOT NULL PRIMARY KEY,
    email NVARCHAR(255),
    name NVARCHAR(255),
    city NVARCHAR(255),
    state NVARCHAR(255),
    registration_datetime DATETIME2
);
GO

-- Fact: Transactions
CREATE TABLE fact_transactions (
    transaction_id UNIQUEIDENTIFIER NOT NULL PRIMARY KEY,
    transaction_datetime DATETIME2,
    customer_id UNIQUEIDENTIFIER,
    product_id UNIQUEIDENTIFIER,
    variation_id UNIQUEIDENTIFIER,
    units DECIMAL(18,2),

    CONSTRAINT fk_transactions_customers
        FOREIGN KEY (customer_id)
        REFERENCES dim_customers(customer_id)
);
GO