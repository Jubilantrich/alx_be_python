import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jbrposdb2"
)

print(mydb.get_server_info())

mycursor = mydb.cursor()
# Execute SQL statements using the execute() method on the cursor

mycursor.execute("SELECT * FROM user2")
myresult = mycursor.fetchall()

for row in myresult:
  print(row)

# Close connection to the databasse  
mycursor.close()
mydb.close()