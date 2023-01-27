from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse #devolver valores html

#CREACION DE LA APP FASTAPI:

app = FastAPI()

@app.get("/", tags=["Home"])


def read_root():
    return HTMLResponse('<h1> Hello Word </h1>')

