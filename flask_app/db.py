import config
from pymongo import MongoClient


client = MongoClient(f"mongodb://{config.USER}:{config.PASSWORD}@{config.HOST}:{config.PORT}/")
db = client["test"]


def get_db():
    return db