from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.planner import router

app = FastAPI(
    title="AI Travel Planner API",
    description="Generate AI-powered travel itineraries with hotel & cost suggestions",
    version="1.0.0"
)

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Travel Planner API 🌍", "docs": "/docs"}
