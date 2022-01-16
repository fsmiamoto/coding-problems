CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    investment NUMERIC
);

CREATE TABLE operations (
    id INTEGER PRIMARY KEY,
    client_id INTEGER REFERENCES clients(id),
    month INTEGER,
    profit NUMERIC
);

INSERT INTO clients (id, name, investment) values
(1, 'Daniel', 500 ),
(2, 'Oliveira', 2000),
(3, 'Lucas', 1000);

INSERT INTO operations (id, client_id, month, profit) values
( 1,    1,  1,  230 ),
( 2,    2,  1,  1000),
( 3,    2,  2,  1000),
( 4,    3,  1,  100 ),
( 5,    3,  2,  300 ),
( 6,    3,  3,  900 ),
( 7,    3,  4,  400 );

-- For sure there's a better way of doing it but hey, it works :D
WITH
tbl AS (
    SELECT name, client_id, month, SUM(profit) OVER (PARTITION BY client_id ORDER BY month) AS cumm_sum, clients.investment
    FROM operations
    JOIN clients ON client_id = clients.id
),
tbl2 AS (SELECT name, month, investment, client_id, (cumm_sum-investment) as return FROM tbl),
tbl3 AS (SELECT name, investment, month as month_of_payback, return, ROW_NUMBER() OVER (PARTITION BY client_id) AS rn FROM tbl2 WHERE return >= 0 ORDER BY return DESC)
SELECT name, investment, month_of_payback, return FROM tbl3 WHERE rn = 1;
