#Connect to the dq database as the user dq
#Using the Cursor object, create a string query that selects all from the notes table.
#Execute the query using the execute method.
#Fetch all the results from the table and assign it to the variable notes.
#Close the Connection using the close method.

import psycopg2
conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()
cur.execute('SELECT * from notes')
notes = cur.fetchall()
conn.close()
