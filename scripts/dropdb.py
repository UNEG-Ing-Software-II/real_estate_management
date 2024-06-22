# This erases all the Railway and local tables, use when the BD is updated
from django.db import connection

def drop_tables():
    with connection.cursor() as cursor:

        cursor.execute("SET session_replication_role = replica;")
        cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
        cursor.execute("SET session_replication_role = DEFAULT;")

    print("All tables have been eliminated, including those with external key restrictions.")

drop_tables()
