import os
from dotenv import load_dotenv
from client.core.Client import Client

if os.environ.get("MODE") is None:
    load_dotenv("../.env")
    print("Load env from .env file")

client = Client()
from client.core.client_exec_task import *
