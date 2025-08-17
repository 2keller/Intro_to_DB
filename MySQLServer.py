import mysql.connector
from mysql.connector import errorcode

def create_database():
    """
    Connects to MySQL server and creates the 'alx_book_store' database.
    """
    try:
        
        cnx = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
        cursor = cnx.cursor()

        db_name = "alx_book_store"

       
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"

        cursor.execute(create_db_query)
        print(f"Database '{db_name}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    
    finally:
       
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'cnx' in locals() and cnx is not None and cnx.is_connected():
            cnx.close()
            print("MySQL connection is closed.")

if __name__ == '__main__':
    create_database()