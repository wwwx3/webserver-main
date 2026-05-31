import psycopg2

host = 'localhost'
dbname = "my_first_db"
user = 'postgres'
password = '123456789'

with psycopg2.connect(host=host, dbname=dbname, user=user, password=password) as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (name, age, salary) VALUES ('Andaman', 18, 25000);")
    conn.commit()

Perfect X
10:29
pip install psycopg2-binary
pip install psycopg[binary]

Perfect X
10:56
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	age INT
);

INSERT INTO users (name, age) VALUES
('Alice', 25),
('Bob', 35),
('Ting Ting', 21);

SELECT * FROM users;

SELECT id,name FROM users;

SELECT * FROM users
WHERE name = 'Alice';

ALTER TABLE users
ADD COLUMN salary INT;

UPDATE users
SET salary = 40000
WHERE id = 1;

UPDATE users
SET salary = 45000
WHERE id = 2 OR id = 3;

SELECT * From users
ORDER BY salary DESC

DELETE FROM users WHERE id = 4;