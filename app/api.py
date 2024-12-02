from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlmodel import Session, select
from src.create_db import Aluguel, Apartamento, DespesaFixa, Garagem, GastoVariavel, Proprietario, engine

# Instância do FastAPI
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

# Rota para inserir um novo apartamento
@app.post("/apartamentos/")
def create_apartamento(apartamentos: Apartamento):
    with Session(engine) as session:
        # Verificar se o apartamento já existe
        existing = session.get(Apartamento, apartamentos.apartamento)
        if existing:
            raise HTTPException(status_code=400, detail="Apartamento já cadastrado")
        
        # Adicionar novo apartamento
        session.add(apartamentos)
        session.commit()
        session.refresh(apartamentos)
        return {"message": "Apartamento inserido com sucesso", "data": apartamentos}

# Rota para inserir um novo proprietário
@app.post("/proprietarios/")
def create_proprietario(proprietarios: Proprietario):
    with Session(engine) as session:
        # Verificar se o proprietário já existe
        existing = session.get(Proprietario, proprietarios.cpf)
        if existing:
            raise HTTPException(status_code=400, detail="Proprietário já cadastrado")
        
        # Adicionar novo proprietário
        session.add(proprietarios)
        session.commit()
        session.refresh(proprietarios)
        return {"message": "Proprietário inserido com sucesso", "data": proprietarios}

# Rota para inserir uma nova despesa fixa
@app.post("/despesas_fixas/")
def create_despesa_fixa(despesas_fixas: DespesaFixa):
    with Session(engine) as session:
        # Verificar se a despesa fixa já existe
        existing = session.get(DespesaFixa, despesas_fixas.id)
        if existing:
            raise HTTPException(status_code=400, detail="Despesa fixa já cadastrada")
        
        # Adicionar nova despesa fixa
        session.add(despesas_fixas)
        session.commit()
        session.refresh(despesas_fixas)
        return {"message": "Despesa fixa inserida com sucesso", "data": despesas_fixas}

# Rota para inserir um novo gasto variável
@app.post("/gastos_variaveis/")
def create_gasto_variavel(gastos_variaveis: GastoVariavel):
    with Session(engine) as session:
        # Verificar se o gasto variável já existe
        existing = session.get(GastoVariavel, gastos_variaveis.id)
        if existing:
            raise HTTPException(status_code=400, detail="Gasto variável já cadastrado")
        
        # Adicionar novo gasto variável
        session.add(gastos_variaveis)
        session.commit()
        session.refresh(gastos_variaveis)
        return {"message": "Gasto variável inserido com sucesso", "data": gastos_variaveis}

# Rota para inserir um novo aluguel
@app.post("/alugueis/")
def create_aluguel(alugueis: Aluguel):
    with Session(engine) as session:
        # Verificar se o aluguel já existe
        existing = session.get(Aluguel, alugueis.id)
        if existing:
            raise HTTPException(status_code=400, detail="Aluguel já cadastrado")
        
        # Adicionar novo aluguel
        session.add(alugueis)
        session.commit()
        session.refresh(alugueis)
        return {"message": "Aluguel inserido com sucesso", "data": alugueis}

# Rota para inserir uma nova locação de garagem
@app.post("/garagens/")
def create_garagem(garagens: Garagem):    
    with Session(engine) as session:
        # Verificar se a garagem já existe
        existing = session.get(Garagem, garagens.id)
        if existing:
            raise HTTPException(status_code=400, detail="Garagem já cadastrada")
        
        # Adicionar nova garagem
        session.add(garagens)
        session.commit()
        session.refresh(garagens)
        return {"message": "Garagem inserida com sucesso", "data": garagens}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"message": "Dados enviados são inválidos!", "details": exc.errors()},
    )
