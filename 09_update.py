import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

# conn.autocommit = True

cursor = conn.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'F'"
cursor.execute(sql)




conn.commit()
conn.close()