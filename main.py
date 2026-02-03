from fastapi import FastAPI
from routers import aqi  # 1. Import the router file
from loguru import logger

app = FastAPI()

# 2. Tell the app to include the router's logic
app.include_router(aqi.router)

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}