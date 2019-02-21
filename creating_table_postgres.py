#Connect to the dq database as the user dq
#Write a SQL query that creates a table called users in the dq database, with the following columns and data types:
#id -- integer data type, and is a primary key.
#email -- text data type.
#name -- text data type.
#address -- text data type.
#Execute the query using the execute method.
#Don't close the connection.

import psycopg2
conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()
cur.execute("CREATE TABLE users(id integer PRIMARY KEY, email text, name text, address text)")
