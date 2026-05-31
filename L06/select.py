import psycopg2

host = 'localhost'
dbname = "my_first_db"
user = 'postgres'
password = '123456789'

with psycopg2.connect(host=host, dbname=dbname, user=user, password=password) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM usersn WHERE id = 1;")
        rows = cur.fetchall()
        print(rows)
        
        for row in rows:
            if "Alice" in row:
                print("Found Alice")
