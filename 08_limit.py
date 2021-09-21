import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

# conn.autocommit = True

cursor = conn.cursor()


cursor.execute('''SELECT * from EMPLOYEE LIMIT 3''')
print(cursor.fetchall())



conn.close()