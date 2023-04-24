from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("general/homepage.html", {"request": request})
