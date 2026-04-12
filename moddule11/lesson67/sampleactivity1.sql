DROP TABLE IF EXISTS supplier;
--  Create two tables "Salesman" & "Orders" and then write a query to display all the orders for the salesman who belongs to the city London.
CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);
INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
('S1', 'Smith', 20, 'London'),
('S2', 'Jones', 10, 'Paris'),
SELECT * FROM supplier;