#Import the psycopg2 library.
#Connect to the dq database with the user dq.
#Use the print function to display the Connection object.
#Close the Connection using the close method.

import psycopg2
Connection = psycopg2.connect("dbname = dq user = dq")
print(Connection)
Connection.close()
