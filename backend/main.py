from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.contact_routes import router as contact_router

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Portfolio Backend API")

# Configure CORS for frontend access
allowed_origins = [
    "https://bhumidigital.netlify.app",
    "https://digital-resume-ruby.vercel.app",
    "https://digital-resume-pwtd.vercel.app",
    "https://digital-resume-ruby-bhumika8982s-projects.vercel.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contact_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Portfolio API"}
