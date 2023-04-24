from services.server import services
from typing import Annotated
from fastapi import FastAPI, Request, Security, HTTPException, Depends, Query
from fastapi.security.api_key import APIKeyHeader, APIKeyQuery, APIKeyCookie
from starlette import status
import os
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import pandas as pd
import requests
load_dotenv()

version = os.getenv('VERSION', 'dev-prueba')

API_KEY = os.getenv('TOKEN', '12345678')
API_KEY_NAME = 'API-KEY'


api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_query_auth = APIKeyCookie(name=API_KEY_NAME, auto_error=False)
api_key_cookie_auth = APIKeyQuery(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
    api_key_query: str = Security(api_key_query_auth),
    api_key_header: str = Security(api_key_header_auth),
    api_key_cookie: str = Security(api_key_cookie_auth)
):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

app = FastAPI(
    title="servicios",
    description="Desarrollo de API ",
    version=version
)
afinidad = {}


class solicitud(BaseModel):
    nombre: str = Query(default=None, max_length=20)
    apellido: str = Query(default=None, max_length=20)
    identificacion: str = Query(default=None, max_length=10)
    edad: int = Field(ge=1, lt=99)
    afinidad: str = Query(default=None, max_length=20)


@app.get("/")
def test():
    df = pd.read_excel("Tipos de Magia.xlsx", index_col=0)
    print(df.index[0])
    return {'message': 'mensaje de prueba'}


@app.post("/solicitud")
def create_solicitud(request: Request, item: solicitud,
                     api_key: bool = Depends(get_api_key)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated")
    build = services()

    result = build.create_solicitud(
        nombre=item.nombre,
        apellido=item.apellido,
        identificacion=item.identificacion,
        edad=item.edad,
        afinidad=item.afinidad,
        )

    return result


@app.put("/solicitud/{id}")
def update_solicitud(id: int, item: solicitud,
                     api_key: bool = Depends(get_api_key)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated")
    build = services()
    result = build.updateSolicitud(id=id,nombre=item.nombre,
        apellido=item.apellido,
        identificacion=item.identificacion,
        edad=item.edad,
        afinidad=item.afinidad)
    return result

@app.put("/estatus/{id}")
def estatus(id: int, estatus:str, api_key: bool = Depends(get_api_key)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated")
    build = services()

    result = build.updatestatus(id,estatus)
    return result

@app.get("/solicitud")
def create_solicitud(api_key: bool = Depends(get_api_key)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated")
    
    build = services()
    result = build.get_solicitud()
    return result


@app.get("/grimorios/{id}")
def update_todo(id: int,
                api_key: bool = Depends(get_api_key)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated")
    build = services()
    result = build.get_grimorios(id=id)
    return result


@app.delete("/solicitud/{id}")
def delete_todo(id: int, api_key: bool = Depends(get_api_key)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated")

    build = services()
    result = build.borrar(id=id)
    return result
