import os
from dotenv import load_dotenv


load_dotenv(".env")

USER = os.environ.get("MONGO_USER")
PASSWORD = os.environ.get("MONGO_PASSWORD")
HOST = os.environ.get("MONGO_HOST")
PORT = os.environ.get("MONGO_PORT")