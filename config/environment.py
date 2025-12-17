import os
from dotenv import load_dotenv

load_dotenv()

db_URI = os.getenv('DATABASE_URL')
secret = os.getenv('JWT_SECRET')