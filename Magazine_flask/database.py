import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(
    host='localhost',
    port=5432,
    database='shop',
    user='postgres',
    password='postgres'
)

with connection:
    cursor = connection.cursor(cursor_factory=RealDictCursor)
