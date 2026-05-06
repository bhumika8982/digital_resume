import os
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from dotenv import load_dotenv

# Force loading .env from the current directory
load_dotenv(dotenv_path='.env')

async def test_connection():
    url = os.getenv("MONGODB_URL")
    if not url:
        print("Error: MONGODB_URL not found in .env file.")
        return
        
    print(f"Attempting to connect to host: {url.split('@')[-1].split('/')[0]}")
    
    client = AsyncIOMotorClient(url, serverSelectionTimeoutMS=5000)
    try:
        # Check if we can even reach the server
        print("Pinging server...")
        await client.admin.command('ping')
        print("Ping successful! (Server is reachable)")
        
        # Check authentication by trying to list databases
        print("Testing authentication...")
        dbs = await client.list_database_names()
        print(f"Authentication Successful! Databases: {dbs}")
        
    except Exception as e:
        print(f"\n--- CONNECTION ERROR ---")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {e}")
        print(f"------------------------\n")
        print("TIPS:")
        print("1. Check if username/password in .env matches MongoDB Atlas 'Database Access' user.")
        print("2. Check if your current IP is whitelisted in 'Network Access'.")
        print("3. Ensure the user has 'Read and write to any database' permissions.")

if __name__ == "__main__":
    asyncio.run(test_connection())
