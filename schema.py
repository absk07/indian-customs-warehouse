def create_schema(my_cursor):
    my_cursor.execute('''
        USE DATABASE INDIAN_CUSTOMS;
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE SCHEMA STAGING_ZONE
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE SCHEMA CURATED_ZONE
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE SCHEMA CONSUMPTION_ZONE
    ''')

    