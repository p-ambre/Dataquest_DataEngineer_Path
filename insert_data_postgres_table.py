#Import the csv module.
#Connect to the dq database as the user dq
#Execute the insert query on the users table using the execute method from the example above.
#Insert every row from the user_accounts.csv file and skip the header row.
#Fetch all the results from the users table and assign it to the variable users.
#Close the Connection using the close method.
import csv
import psycopg2

with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    rows = [row for row in reader]

conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()

for row in rows:
    cur.execute("INSERT INTO users VALUES (%s,%s,%s,%s)", row)
conn.commit()

cur.execute('SELECT * FROM users')
users = cur.fetchall()
conn.close()
