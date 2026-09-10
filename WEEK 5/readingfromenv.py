import os
from dotenv import load_dotenv

load_dotenv("WEEK 5/ .env")

api_key= os.getenv("FB_ACCESS_TOKEN")
print(api_key)