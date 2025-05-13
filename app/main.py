from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import root  # 라우터 임포트

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 라우터 등록
app.include_router(root.router)
