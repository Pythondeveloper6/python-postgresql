import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

# conn.autocommit = True

cursor = conn.cursor()

cursor.execute('''DELETE FROM EMPLOYEE WHERE AGE > 27''')





conn.commit()
conn.close()