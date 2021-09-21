import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

# conn.autocommit = True

cursor = conn.cursor()

cursor.execute("DROP TABLE EMPLOYEE")




conn.commit()
conn.close()