from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import asyncio

from app.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION

def create_app():
  app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
  app.mount("/static", StaticFiles(directory="static"))
  templates = Jinja2Templates(directory="templates") 

  @app.on_event("startup")
  async def poll_bus():
    # Put polling code here
    await asyncio.sleep(1)
    asyncio.create_task(poll_bus())

  @app.get("/")
  async def index(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })

  return app

app = create_app()
