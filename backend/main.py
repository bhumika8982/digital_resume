from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.contact_routes import router as contact_router

app = FastAPI(title="Portfolio Backend API")

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contact_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Portfolio API"}
