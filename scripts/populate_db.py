import os
import sys
import django
import json

# Configure the base route of the project (a backward directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configure Django's environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyR.settings")
django.setup()

from app import models

ARGS = [
    {
        "key": "tasks",
        "file": BASE_DIR + "\\app\\data\\tasks.json",
        "model": models.Task,
    },
    {
        "key": "features",
        "file": BASE_DIR + "\\app\\data\\features.json",
        "model": models.Feature,
    },
    {
        "key": "estate",
        "file": BASE_DIR + "\\scripts\\estates.json",
        "model": models.Estate,
    },
    {
        "key": "users",
        "file": BASE_DIR + "\\scripts\\users.json",
        "model": models.User,
        "function": models.User.objects.create_user,
    },
]

if len(sys.argv) > 1:
    ARGS = [*filter(lambda arg: arg["key"] in sys.argv, ARGS)]

for item in ARGS:
    data = json.loads(open(item["file"]).read())
    for registry in data:
        try:
            model = (
                item["function"](**registry)
                if item.get("function")
                else item["model"].objects.create(**registry)
            )
            print(
                "%s (%s) Created satisfactorily"
                % (model.__str__(), item["key"].upper())
            )
        except Exception as e:
            print(str(e))
