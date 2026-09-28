-- DISTINCT — distinct acquisition_source values used across all customers. — 1 mark Expected: exactly 4 values — Ad, Organic, Referral, Social.

SELECT DISTINCT acquisition_source
FROM customers;