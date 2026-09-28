-- total_orders = 180, total_revenue = 99860.20, avg_order_value = 554.78
SELECT
    COUNT(*) AS total_orders,
    SUM(
        o.quantity * p.price *
        (1 - COALESCE(o.discount_pct, 0) / 100)
    ) AS total_revenue,
    AVG(
        o.quantity * p.price *
        (1 - COALESCE(o.discount_pct, 0) / 100)
    ) AS avg_order_value
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;