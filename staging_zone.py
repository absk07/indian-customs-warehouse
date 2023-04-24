def create_stage(my_cursor):
    my_cursor.execute('''
        USE DATABASE INDIAN_CUSTOMS;
    ''')

    my_cursor.execute('''
        USE SCHEMA STAGING_ZONE;
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE STAGE stage_importexport;
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE STAGE stage_type;
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE STAGE stage_tax;
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE STAGE stage_category;
    ''')