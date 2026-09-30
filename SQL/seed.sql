-- seed_data.sql

-- 1. Configure SQLite CLI for CSV import
.mode csv

-- 2. Import CSV data into tables
.import data/customers.csv customers
.import data/products.csv products
.import data/orders.csv orders

-- 3. Post-import cleanup: Convert empty string imports to SQL NULL
-- SQLite's .import treats blank CSV fields as empty strings (''). 
-- Explicitly setting them to NULL ensures aggregates like COUNT(rating) remain accurate.
UPDATE orders SET discount_pct = NULL WHERE discount_pct = '';
UPDATE orders SET rating = NULL WHERE rating = '';

-- 4. Verification checks
SELECT COUNT(*) AS total_customers FROM customers; -- Expected: 45
SELECT COUNT(*) AS total_products FROM products;   -- Expected: 16
SELECT COUNT(*) AS total_orders FROM orders;       -- Expected: 180

-- Confirm NULL handling for rating column
SELECT typeof(rating), COUNT(rating) FROM orders WHERE rating IS NULL;
