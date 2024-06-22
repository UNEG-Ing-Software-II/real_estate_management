# This erases all the Railway and local tables, use when the BD is updated
import os
import sys
from django.db import connection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyR.settings")

def drop_tables():
    with connection.cursor() as cursor:

        cursor.execute("SET session_replication_role = replica;")
        cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
        cursor.execute("SET session_replication_role = DEFAULT;")

    print("All tables have been eliminated, including those with external key restrictions.")

drop_tables()
