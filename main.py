from enum import Enum
import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles


class ModelName(str, Enum):
    pyramid = "pyramid"
    cube = "cube"
    star = "star"
    sphere = 'sphere'


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/{model_name}")
async def get_model(request: Request, model_name: ModelName):
    context = {'figure': model_name.value, "request": request}
    return templates.TemplateResponse("main.html", context=context)

    #return {"model_name": model_name, "message": "Have some residuals"}
