from fastapi import FastAPI
import logging

app = FastAPI()

logger = logging.getLogger("uvicorn")

@app.get("/")
async def root():
    logger.debug("DEBUG 로그입니다.")
    logger.info("INFO 로그입니다.")
    return {"message": "Hello World"}