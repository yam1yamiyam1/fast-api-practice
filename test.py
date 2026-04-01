import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from fastapi import FastAPI
from training_data import users

user_lookup = {u["id"]: u for u in users}
app = FastAPI()
app.get("/get-user/{user_id}")


def get_user(user_id: int):
    return user_lookup.get(user_id)
