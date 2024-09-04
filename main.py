"""
This is the main module of my application.
It contains the entry point of the program.
"""
from enum import Enum
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles


class ModelName(str, Enum):
    """
    Все возможные фигуры
    """
    PYRAMID = "pyramid"
    CUBE = "cube"
    STAR = "star"
    SPHERE = 'sphere'


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/{model_name}")
async def get_model(request: Request, model_name: ModelName):
    '''
    Функция переключения ендпоинтов
    '''
    context = {'figure': model_name.value}
    return templates.TemplateResponse(request, "main.html", context=context)
