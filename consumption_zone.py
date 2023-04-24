def create_consumption_zone(my_cursor):
    my_cursor.execute('''
        USE DATABASE INDIAN_CUSTOMS;
    ''')

    my_cursor.execute('''
        USE SCHEMA CONSUMPTION_ZONE;
    ''')

    # create type dimension table
    my_cursor.execute('''
        CREATE OR REPLACE TABLE DIM_TYPE(
            type INTEGER,
            name STRING
        )
    ''')

    # create category dimension table
    my_cursor.execute('''
        CREATE OR REPLACE TABLE DIM_CATEGORY(
            category_id INTEGER,
            category_name STRING,
            important INTEGER
        )
    ''')

    # create tax dimension table
    my_cursor.execute('''
        CREATE OR REPLACE TABLE DIM_TAX(
            category_id INTEGER,
            tax_in_per INTEGER
        )
    ''')

    # create importexport fact table
    my_cursor.execute('''
        CREATE OR REPLACE TABLE FACT_IMPORTEXPORT (
            serialid INTEGER,
            date DATETIME,
            year STRING,
            month STRING,
            day STRING,
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

    # copy required colums from curated_zone.category to the dim_category table
    my_cursor.execute('''
        INSERT INTO DIM_CATEGORY(category_id, category_name, important)
        SELECT
            category_id,
            category_name,
            important
        FROM CURATED_ZONE.CATEGORY;
    ''')

    # copy required colums from curated_zone.type to the dim_type table
    my_cursor.execute('''
        INSERT INTO DIM_TYPE(type, name)
        SELECT
            type,
            name
        FROM CURATED_ZONE.TYPE;
    ''')

    # copy required colums from curated_zone.tax to the dim_tax table
    my_cursor.execute('''
        INSERT INTO DIM_TAX(category_id, tax_in_per)
        SELECT
            category_id,
            tax_in_per
        FROM CURATED_ZONE.TAX;
    ''')

    # copy required colums from curated_zone.importexport to the dim_importexport table
    my_cursor.execute('''
        INSERT INTO FACT_IMPORTEXPORT(
            serialid,
            date,
            year,
            month,
            day,
            ind_location_state,
            ind_location_code,
            ind_location_name,
            foreign_country,
            type,
            customs_tariff_heading,
            unit_quantity_code,
            quantity,
            quantity_desc,
            quantity_type,
            value_of_goods_in_rupees,
            category_id,
            is_returnable,
            is_returned,
            is_ban
        )
        SELECT
            serialid,
            date,
            YEAR(date),
            MONTH(date),
            DAY(date),
            ind_location_state,
            ind_location_code,
            ind_location_name,
            foreign_country,
            type,
            customs_tariff_heading,
            unit_quantity_code,
            quantity,
            quantity_desc,
            quantity_type,
            value_of_goods_in_rupees,
            category_id,
            is_returnable,
            is_returned,
            is_ban
        FROM CURATED_ZONE.IMPORTEXPORT;
    ''')