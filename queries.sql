-- Task 1a: Retrieve all columns from the products table
SELECT *
FROM products;

-- Task 1b: Retrieve the names and phone numbers of all shippers
SELECT name, phone
FROM shippers;

-- Task 2: Find the average, maximum, and minimum price of products
SELECT
    AVG(price) AS avg_price,
    MAX(price) AS max_price,
    MIN(price) AS min_price
FROM products;

--  Task 3: List the top 10 most expensive products along with their category IDs
SELECT DISTINCT
    category_id,
    price
FROM products
ORDER BY price DESC
LIMIT 10;

-- Task 4: Count the number of products with a price between $20 and $100
SELECT
    COUNT(*) AS product_count
FROM products
WHERE price > 20 AND price < 100

-- Task 5: For each supplier, list the number of products they supply and the average price of those products
SELECT
    supplier_id,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM products
GROUP BY supplier_id;