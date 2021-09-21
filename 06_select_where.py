import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

# conn.autocommit = True

cursor = conn.cursor()


cursor.execute("SELECT * from EMPLOYEE WHERE AGE <28")
print(cursor.fetchall())



conn.close()