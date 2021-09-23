import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

# conn.autocommit = True

cursor = conn.cursor()


cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,INCOME) 
                               VALUES ('mahmoud', 'ahmed', 27, 'M', 9000)''')


cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,INCOME) 
                               VALUES ('Aya', 'Mohamed', 26, 'F', 10000)''')

conn.commit()
conn.close()
