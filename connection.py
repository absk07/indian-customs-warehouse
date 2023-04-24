import snowflake.connector
from dotenv import load_dotenv
import os

load_dotenv()

def db_connect():
    connection = snowflake.connector.connect(
        user = os.getenv('SNOWFLAKE_USERNAME'),
        password = os.getenv('SNOWFLAKE_PASSWORD'),
        account = os.getenv('SNOWFLAKE_ACCOUNT')
    )
    return connection