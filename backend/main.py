from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from router import router
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Gestão Imobiliária",
    description="API para gerenciar apartamentos, despesas e aluguéis.",
    version="1.0.0",
    contact={
        "name": "Roberto German Guedes Neto",
        "email": "robertoguedes@edu.univali.br",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def normalize_request_data(request: Request, call_next):
    if request.headers.get("content-type") == "application/json":
        body = await request.body()
        if body:
            normalized_body = json.dumps(json.loads(body.decode("utf-8")))
            request._body = normalized_body.encode("utf-8")
    return await call_next(request)

@app.middleware("http")
async def log_request_data(request: Request, call_next):
    body = await request.json()
    print(f"Requisição recebida: {body}")
    response = await call_next(request)
    return response