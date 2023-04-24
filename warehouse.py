def create_warehouse(my_cursor):
    my_cursor.execute('USE ROLE ACCOUNTADMIN;')

    my_cursor.execute('''
        CREATE WAREHOUSE IMPORT_EXPORT WITH
        WAREHOUSE_SIZE = 'LARGE'
        WAREHOUSE_TYPE = 'STANDARD' 
        AUTO_SUSPEND = 300 
        AUTO_RESUME = TRUE;
    ''')