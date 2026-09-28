SELECT
    p.category,
    COUNT(o.order_id) AS order_count,
    SUM(o.quantity * p.price) AS category_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY p.category
ORDER BY category_revenue DESC;