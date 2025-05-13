from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core.template import templates  # 공통 템플릿 객체 import

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
