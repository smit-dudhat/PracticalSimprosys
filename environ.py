from dotenv import load_dotenv
from pathlib import Path
import os

print()
BASE_DIR = os.getcwd().replace('\\','/')


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
TEMPLATE_DIR = BASE_DIR + '/templates'
