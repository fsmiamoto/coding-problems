--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2737

CREATE TABLE lawyers(
  register INTEGER PRIMARY KEY,
  name VARCHAR(255),
  customers_number INTEGER
 );


 INSERT INTO lawyers(register, name, customers_number)
 VALUES (1648, 'Marty M. Harrison', 5),
	(2427, 'Jonathan J. Blevins', 15),
	(3365, 'Chelsey D. Sanders', 20),
	(4153, 'Dorothy W. Ford', 16),
	(5525, 'Penny J. Cormier', 6);

--- Solution
(SELECT name, customers_number FROM lawyers ORDER BY customers_number DESC LIMIT 1)
UNION ALL
(SELECT name, customers_number FROM lawyers ORDER BY customers_number ASC LIMIT 1)
UNION ALL
(SELECT 'Average' AS name, CAST(AVG(customers_number) AS INT) AS customers_number FROM lawyers);

--- Clean up
DROP TABLE lawyers;
