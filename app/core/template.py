from datetime import datetime

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")


def format_unix_timestamp(value):
    return datetime.utcfromtimestamp(value).strftime("%Y-%m-%d %H:%M:%S")


# 템플릿에서 쓸 공통 객체추가
templates.env.filters["datetime"] = format_unix_timestamp
