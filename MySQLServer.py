import mysql.connector
from mysql.connector import errorcode

# Database configuration
db_config = {
    'user': 'your_username',  # replace with your username
    'password': 'your_password',  # replace with your password
    'host': 'localhost',  # or your host
    'raise_on_warnings': True
}

# Try to create the database
try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    # Close the cursor and connection if they were opened
    if cursor:
        cursor.close()
    if connection:
        connection.close()
