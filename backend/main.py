from fastapi import FastAPI
from database import engine
import models
from router import router

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