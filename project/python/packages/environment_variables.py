
#---This is a simple example of how to connect to a database using environment variables.

# set environment variables - 1 way
'''os.environ['DB_HOST'] = 'localhost'
os.environ['DB_USER'] = 'root'
os.environ['DB_PASSWORD'] = 'root'
os.environ['DB_NAME'] = 'testdb'
'''
'''set environment variables - 2 way
export DB_HOST='localhost'
export DB_USER='root'
export DB_PASSWORD='root'
export DB_NAME='testdb'
'''
'''import os
import mysql.connector
# Get environment variables
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

# Connect to the database

connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name 
)
print("connected to the database")
connection.close()'''