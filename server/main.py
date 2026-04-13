from fastapi import FastAPI
from features.research.routes import router as research_router

# App instance
app = FastAPI()

# Health-check endpoint
@app.get("/api/health-check")
def health_check():
    return {
        "status": "ok",
        "name": "Research Agent API"
    }

# Mount routers
app.include_router(
    router=research_router,
    prefix="/api/research"
)

