from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.contact_routes import router as contact_router

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Portfolio Backend API")

# Configure CORS for frontend access
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "http://localhost:3000"], # Allow production and local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contact_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Portfolio API"}
