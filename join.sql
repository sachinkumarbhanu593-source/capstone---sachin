-- LEFT JOIN with a genuine zero-match row — LEFT JOIN customers to orders, GROUP BY customer, HAVING COUNT(order_id) = 0, to find any customer with zero orders. Then write a second, independent query using NOT IN (SELECT DISTINCT customer_id FROM orders) that must return the same customer, confirming the LEFT JOIN result rather than trusting it blindly. — 3 marks Expected: both queries return exactly one row — C045, Vihaan.


SELECT
    c.customer_id,
    c.name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.name
HAVING COUNT(o.order_id) = 0;

SELECT
    customer_id,
    name
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id
    FROM orders
);