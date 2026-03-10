"""
HN-Claw-Stock Backend API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.config import settings
from app.api.stocks import router as stocks_router
import os

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-Powered US Stock Selection & Trading Suggestions"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the frontend directory (absolute path)
FRONTEND_DIR = "/home/admin/HN-Claw-Stock/frontend"


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the frontend HTML"""
    frontend_file = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(frontend_file):
        with open(frontend_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>Frontend not found</h1>", status_code=404)


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Include routers
app.include_router(stocks_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
