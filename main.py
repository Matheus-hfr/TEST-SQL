from db_connection import create_connection, execute_query, insert_data, fetch_data,update_data,delete_data

def main():
    database = "educational_system.db"  # Name of the database file
    connection = create_connection(database)

    if connection:
        # Create the table if it doesn't already exist                                      LINHA 10 ATE 25----------- code of the create table
        create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        );
        """
        execute_query(connection, create_students_table)

        # Insert a new student into the table
        insert_student_query = "INSERT INTO students (name, age) VALUES (?, ?);"
        student_to_insert = [("John Doe", 20),
                             ('Alice Smith', 22),
                             ('Bob Brown', 25)
                             ]
        for student in student_to_insert:
            insert_data(connection, insert_student_query, student)

        select_students_query = 'SELECT * FROM students;'
        students = fetch_data(connection,select_students_query)

        print('List of Students')                               #STUDENTS OF LIST BEFORE THE CHANGES
        print('----------------')
        for student in students:
            print(f'ID: {student[0]}, Name: {student[1]}, Age: {student[2]}')

        update_student_query = 'UPDATE students SET age = ? WHERE name = ?'
        student_data_to_update = (25, 'John Doe')
        update_data(connection, update_student_query, student_data_to_update)                    #UPDATE FUNCTION EXAMPLE

        students = fetch_data(connection,select_students_query)

        print("\nList of Students After Update:")
        print("-------------------------------")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")

        delete_student_query = 'DELETE FROM students WHERE name = ?'                 #The query DELETE FROM students WHERE name = ?; deletes a student based on their name.
        student_to_delete = ('Alice Smith',)                                         #Specifies the name of the student to remove
        delete_data(connection,delete_student_query,student_to_delete)

        students = fetch_data(connection,select_students_query)

        print("\nList of Students After Deletion:")
        print("--------------------------------")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")


        connection.close()
        print("Connection closed successfully.")

if __name__ == "__main__":
    main()
