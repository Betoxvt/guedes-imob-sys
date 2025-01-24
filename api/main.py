from database import engine, trigger_aluguel, verify_trigger
from fastapi import FastAPI
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


@app.on_event("startup")
async def startup_event():
    with engine.connect() as conn:
        try:
            result = conn.execute(verify_trigger)
            if result.fetchone() is None:
                conn.execute(trigger_aluguel)
                conn.commit()
                print("Trigger criado com SUCESSO")
            else:
                print("Trigger já existe")
        except Exception as e:
            conn.rollback()
            print(f"ERRO ao criar o trigger: {e}")


app.include_router(router)
