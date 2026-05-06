from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "your_mongodb_atlas_url_here")

if not MONGODB_URL or MONGODB_URL == "your_mongodb_atlas_url_here":
    print("Warning: MONGODB_URL not set. Database connection will fail.")

client = AsyncIOMotorClient(MONGODB_URL)
db = client.portfolio_db
contact_collection = db.get_collection("contacts")
