import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jbrposdb2"
)

print(mydb.get_server_info())