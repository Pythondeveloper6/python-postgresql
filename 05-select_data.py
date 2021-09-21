import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

# conn.autocommit = True

cursor = conn.cursor()


cursor.execute('''SELECT * from EMPLOYEE''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)


#Fetching 1st row from the table
result = cursor.fetchall();
print(result)


conn.close()