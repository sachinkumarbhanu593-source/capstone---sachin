--  COUNT(*) vs COUNT(column) — one query showing COUNT(*), COUNT(rating), and the difference, on orders. — 2 marks Expected: (180, 165, 15) — 15 orders have no rating yet.

SELECT
    COUNT(*) AS total_rows,
    COUNT(rating) AS rated_orders,
    COUNT(*) - COUNT(rating) AS unrated_orders
FROM orders;