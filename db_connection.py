import sqlite3 
from sqlite3 import Error

def create_connection(db_file):
    '''
    
    # Creates a connection to the SQLite Database.
    # If the database file does not exist,it will be created

    db_file : Path to the database file.
    return : connection object or None in case of an error.
    '''

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f'Connection established to the database: {db_file}')
    except Error as e:
        print(f'Error connection to the database: {e}')
    return connection

def execute_query(connection, query):
    '''
    
    Executes a single SQL query (e.g. , CREATE TABLE).

    connection : SQlite connection object
    query: The SQL query to execute.
    '''

    try:
        cursor = connection.cursor() #Create a cursor object from the database connection . The cursor is used to interact with o database.It allows you to execute commands ( SELECT,INSERT ...)
        cursor.execute(query) # executes the SQL query passed to the execute() method.
        connection.commit() #ensures that those changes are written permanently to the database file.
        print('Query executed sucessfully')
    except Error as e:
        print(f'Error executing query: {e}')

def insert_data(connection, query, data):
    '''
    Insert data into a table using a parameterized SQL query

    :param connection: SQLite connection object.
    :param query: The SQL INSERT query.
    :param data: Tuple of data values to insert.
    '''
    try:
        cursor = connection.cursor() #Create a cursor object from the database connection.
        cursor.execute(query,data) #executes a SQL query passed to the execute() method.
        connection.commit() #ensures that those changes are written permanently.
    except Error as e:
        print (f'Error inserting data: {e}')

def fetch_data(connection, query):
    '''
    Fetches data from the database using a SELECT query

    :param connection: SQLite connection object.
    :param query: The SQL SELECT query.
    :return: List of rows retrieved by the query.
    
    '''

    try:
        cursor = connection.cursor()  # Create a cursor object from the database connection.
        cursor.execute(query)    # executes a SQL query passed to the execute() method.
        rows = cursor.fetchall() # used to fetch all rows resulting from a query executed. Each tuple represents a row from the database table.
        print('Data rertieved sucessfully.')
        return rows
    except Error as e:
        print(f'Error retreving data: {e}')
        return []

def update_data(connection, query, data):
    '''
    Update existing data in the table using a parameterized SQL query.

    :param connection: SQLite connection object.
    :param query: The SQL UPDATE query.
    :param data: Tuple of new values to update.
    '''
    try:
        cursor = connection.cursor()  # Create a cursor object from the database connection.
        cursor.execute(query, data)  # Executes the SQL query passed to the execute() method.
        connection.commit()  # Ensures that those changes are written permanently.
        print("Data updated successfully")
    except Error as e:
        print(f"Error updating data: {e}")
    
def delete_data(connection,query,data):
    '''
    Deletes data from a table using a parameterized SQL query

    :param connection: SQLite connection object.
    :param query: The SQL DELETE query.
    :param data: Tuple of values to use in the query.
    '''

    try:
        cursor = connection.cursor()     # Create a cursor object from the database connection.
        cursor.execute(query,data)  # Execute the SQL query passed to the execute() method.
        connection.commit()          # Ensure that those changes are written permanently.
        print('Data deleted sucessfully.')
    except Error as e:
        print(f'Error deleting data: {e}')
 
    except Error as e:
        print(f"Error altering table structure: {e}")