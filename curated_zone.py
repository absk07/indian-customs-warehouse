def create_curated_zone(my_cursor):
    my_cursor.execute('''
        USE DATABASE INDIAN_CUSTOMS;
    ''')

    my_cursor.execute('''
        USE SCHEMA CURATED_ZONE;
    ''')

    # create IMPORTEXPORT table and copy data from the stage import_export_stage
    my_cursor.execute('''
        CREATE OR REPLACE TRANSIENT TABLE IMPORTEXPORT (
            serialid INTEGER,
            date DATETIME,
            ind_location_state STRING,
            ind_location_code STRING,
            ind_location_name STRING,
            foreign_country STRING,
            type INTEGER,
            customs_tariff_heading INTEGER,
            unit_quantity_code STRING,
            quantity FLOAT,
            quantity_desc STRING,
            quantity_type STRING,
            value_of_goods_in_rupees FLOAT,
            category_id	INTEGER,
            is_returnable BOOLEAN,
            is_returned BOOLEAN,
            is_ban BOOLEAN
        );
    ''')

    my_cursor.execute('''
        COPY INTO IMPORTEXPORT
        FROM @~/stage_importexport5
        file_format = (type = csv field_delimiter = ',' skip_header = 1);
    ''')

    # create TYPE table and copy data from the stage type_stage
    my_cursor.execute('''
        CREATE OR REPLACE TRANSIENT TABLE TYPE (
            type INTEGER,
            name STRING
        );
    ''')

    my_cursor.execute('''
        COPY INTO TYPE
        FROM @~/stage_type
        file_format = (type = csv field_delimiter = ',' skip_header = 1);
    ''')

    # create category_json_raw table for json data and copy data from the stage category_stage
    # then flatten the json data into rows and columns using snowflake's JSON capabilities
    my_cursor.execute('''
        CREATE OR REPLACE TRANSIENT TABLE category_json_raw (
            category_data VARIANT
        );
    ''')

    my_cursor.execute('''
        COPY INTO category_json_raw
        FROM @~/stage_category
        file_format = (type = json);
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE TRANSIENT TABLE CATEGORY AS
        SELECT
            VALUE:category_id::INTEGER AS category_id,
            VALUE:category_name::String AS category_name,
            VALUE:important::String AS important
        FROM
            category_json_raw,
            lateral flatten(input => category_data);
    ''')

    # create tax_json_raw table for json data and copy data from the stage tax_stage
    # then flatten the json data into rows and columns using snowflake's JSON capabilities
    my_cursor.execute('''
        CREATE OR REPLACE TRANSIENT TABLE tax_json_raw (
            tax_data VARIANT
        );
    ''')

    my_cursor.execute('''
        COPY INTO tax_json_raw
        FROM @~/stage_tax
        file_format = (type = json);
    ''')

    my_cursor.execute('''
        CREATE OR REPLACE TRANSIENT TABLE TAX AS
        SELECT
            VALUE:category_id::INTEGER AS category_id,
            VALUE:tax_in_per::INTEGER AS tax_in_per
        FROM
            tax_json_raw,
            lateral flatten(input => tax_data);
    ''')