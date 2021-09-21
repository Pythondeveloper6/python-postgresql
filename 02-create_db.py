import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Test",
    user="postgres",
    password="toor")

conn.autocommit = True

cursor = conn.cursor()


sql = '''CREATE database mydb2''';


cursor.execute(sql)

conn.close()