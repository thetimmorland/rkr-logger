from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import can
import asyncio

from app.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION

def create_app():
  app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

  can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
  dbWriter = can.SqliteWriter("db.sqlite")
  notifier = can.Notifier(can0, [dbWriter], asyncio.get_event_loop())

  @app.on_event("shutdown")
  async def shutdown():
    notifier.stop()
    dbWriter.stop()
    can0.shutdown()

  app.mount("/static", StaticFiles(directory="static"))
  templates = Jinja2Templates(directory="templates") 

  @app.get("/")
  async def index(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })

  return app

app = create_app()
