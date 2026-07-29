from fastapi import FastAPI

from backend.database import Base, engine

# Import Models
from backend.models.user import User
from backend.models.ct_scan import CTScan

# Import Routers
from backend.routers.user import router as user_router
from backend.routers.ct_scan import router as ct_scan_router

# Create Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PancreAI")

# Routers
app.include_router(user_router)
app.include_router(ct_scan_router)


@app.get("/")
def home():
    return {
        "message": "PancreAI Backend Running 🚀"
    }