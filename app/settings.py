import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

env_vars_loaded = load_dotenv(os.path.join(BASE_DIR, 'ticket_mgmt.env'))
if not env_vars_loaded:
    print("Unable to load environment variables from ticket_mgmt.env, program will exit now.")
    exit(1)

APP_NAME = "tickets_manager"
ENV = os.environ.get("ENV", "DEV") # Default env is DEV

# For in-memory database just two slash characters (//) and no file name:
# SQLALCHEMY_DATABASE_URL = "sqlite://"

# Persistent database -> all the data is saved in a file database.db
SQLALCHEMY_DATABASE_URL = "sqlite:///database.db"

LOGS_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

LOGS_LEVEL = os.environ.get("LOGS_LEVEL", "DEBUG") # Default logs level is DEBUG

