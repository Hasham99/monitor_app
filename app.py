import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env

# Use the variables
GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')