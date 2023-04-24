from connection import db_connect
from warehouse import create_warehouse
from database import create_database
from schema import create_schema
from staging_zone import create_stage
from curated_zone import create_curated_zone
from consumption_zone import create_consumption_zone

try:
    my_cursor = db_connect().cursor()

    create_warehouse(my_cursor)

    create_database(my_cursor)

    create_schema(my_cursor)

    create_stage(my_cursor)

    # use snowsql to load internal data to staging_zone
    
    # put file://C:\Users\abhishek\Desktop\IndianCustoms-Import-Export\Data\ImportExport.csv @~/stage_importexport;
    # put file://C:\Users\abhishek\Desktop\IndianCustoms-Import-Export\Data\type.csv @~/stage_type;
    # put file://C:\Users\abhishek\Desktop\IndianCustoms-Import-Export\Data\category.json @~/stage_category;
    # put file://C:\Users\abhishek\Desktop\IndianCustoms-Import-Export\Data\tax.json @~/stage_tax;

    create_curated_zone(my_cursor)

    create_consumption_zone(my_cursor)
except Exception as e:
    print("############################################################################################")
    print(e)
    print("############################################################################################")
finally:
    db_connect().close()

# my_cursor.execute('USE DATABASE INDIAN_CUSTOMS;')
# my_cursor.execute('''
#         SELECT 
#             i.serialid, i.date, i.year, i.month, i.day, i.ind_location_state, i.ind_location_code, i.ind_location_name, 
#             i.foreign_country, i.type, i.customs_tariff_heading, i.unit_quantity_code, i.quantity, 
#             i.quantity_desc, i.quantity_type, i.value_of_goods_in_rupees, i.category_id, 
#             i.is_returnable, i.is_returned, i.is_ban,
#             c.category_name, c.important,
#             t.tax_in_per,
#             ty.name
#         FROM CONSUMPTION_ZONE.FACT_IMPORTEXPORT i
#         JOIN CONSUMPTION_ZONE.DIM_CATEGORY c ON i.category_id = c.category_id
#         JOIN CONSUMPTION_ZONE.DIM_TYPE ty ON i.type = ty.type
#         JOIN CONSUMPTION_ZONE.DIM_TAX t ON i.category_id = t.category_id
#         ORDER BY i.serialid;
# ''')

# for row in my_cursor.fetchall():
#     print(row)