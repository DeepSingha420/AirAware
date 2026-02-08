from fastapi import FastAPI
from routers import aqi
from loguru import logger

app = FastAPI()

app.include_router(aqi.router)

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called")

    return {"status": "ok"}
