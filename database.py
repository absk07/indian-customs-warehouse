def create_database(my_cursor):
    my_cursor.execute('USE WAREHOUSE IMPORT_EXPORT;')

    my_cursor.execute('''
        CREATE DATABASE INDIAN_CUSTOMS;
    ''')