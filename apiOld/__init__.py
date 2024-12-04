from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlmodel import Session, select
from schemasOld import Aluguel, Apartamento, DespesaFixa, Garagem, GastoVariavel, Proprietario, AluguelPatch, ApartamentoPatch, DespesaFixaPatch, GaragemPatch, GastoVariavelPatch, ProprietarioPatch
from src import engine

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

# Inserir dados nas tabelas

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

# Tratamento de erros
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"message": "Dados enviados são inválidos!", "details": exc.errors()},
    )

# Visualizar dados das tabelas

# Rota para visualizar os alugueis
@app.get("/alugueis/", response_model=list[Aluguel])
def get_alugueis():
    with Session(engine) as session:
        return session.exec(select(Aluguel)).all()

# Rota para visualizar os apartamentos
@app.get("/apartamentos/", response_model=list[Apartamento])
def get_apartamentos():
    with Session(engine) as session:
        return session.exec(select(Apartamento)).all()

# Rota para visualizar as despesas fixas
@app.get("/despesas_fixas/", response_model=list[DespesaFixa])
def get_despesas_fixas():
    with Session(engine) as session:
        return session.exec(select(DespesaFixa)).all()

# Rota para visualizar as locações de garagem
@app.get("/garagens/", response_model=list[Garagem])
def get_garagens():
    with Session(engine) as session:
        return session.exec(select(Garagem)).all()

# Rota para visualizar os gastos variáveis
@app.get("/gastos_variaveis/", response_model=list[GastoVariavel])
def get_gastos_variaveis():
    with Session(engine) as session:
        return session.exec(select(GastoVariavel)).all()

# Rota para visualizar os proprietários
@app.get("/proprietarios/", response_model=list[Proprietario])
def get_proprietarios():    
    with Session(engine) as session:
        return session.exec(select(Proprietario)).all()
    
# Atualizar dados das tabelas

# Rota para atualizar um aluguel
@app.patch("/alugueis/{aluguel_id}")
def patch_aluguel(aluguel_id: int, alugueis: AluguelPatch):
    with Session(engine) as session:
        aluguel = session.get(Aluguel, aluguel_id)
        if not aluguel:
            raise HTTPException(status_code=404, detail="Aluguel não encontrado")
        
        for key, value in alugueis.model_dump(exclude_unset=True).items():
            setattr(aluguel, key, value)
        
        session.add(aluguel)
        session.commit()
        session.refresh(aluguel)
        return {"message": "Aluguel atualizado com sucesso", "data": aluguel}

# Rota para atualizar um apartamento
@app.patch("/apartamentos/{apartamento_id}", response_model=Apartamento)
def patch_apartamento(apartamento_id: str, apartamentos: ApartamentoPatch):
    with Session(engine) as session:
        apartamento = session.get(Apartamento, apartamento_id)
        if not apartamento:
            raise HTTPException(status_code=404, detail="Apartamento não encontrado")
        
        for key, value in apartamentos.model_dump(exclude_unset=True).items():
            setattr(apartamento, key, value)
        
        session.add(apartamento)
        session.commit()
        session.refresh(apartamento)
        return {"message": "Apartamento atualizado com sucesso", "data": apartamento}

# Rota para atualizar uma despesa fixa
@app.patch("/despesas_fixas/{despesa_fixa_id}", response_model=DespesaFixa)
def patch_despesa_fixa(despesa_fixa_id: int, despesas_fixas: DespesaFixaPatch):
    with Session(engine) as session:
        despesa_fixa = session.get(DespesaFixa, despesa_fixa_id)
        if not despesa_fixa:
            raise HTTPException(status_code=404, detail="Despesa fixa não encontrada")
        
        for key, value in despesas_fixas.model_dump(exclude_unset=True).items():
            setattr(despesa_fixa, key, value)
        
        session.add(despesa_fixa)
        session.commit()
        session.refresh(despesa_fixa)
        return {"message": "Despesa fixa atualizada com sucesso", "data": despesa_fixa}

# Rota para atualizar uma locação de garagem
@app.patch("/garagens/{garagem_id}", response_model=Garagem)
def patch_garagem(garagem_id: int, garagens: GaragemPatch):
    with Session(engine) as session:
        garagem = session.get(Garagem, garagem_id)
        if not garagem:
            raise HTTPException(status_code=404, detail="Garagem não encontrada")
        
        for key, value in garagens.model_dump(exclude_unset=True).items():
            setattr(garagem, key, value)
        
        session.add(garagem)
        session.commit()
        session.refresh(garagem)
        return {"message": "Garagem atualizada com sucesso", "data": garagem}

# Rota para atualizar um gasto variável
@app.patch("/gastos_variaveis/{gasto_variavel_id}", response_model=GastoVariavel)
def patch_gasto_variavel(gasto_variavel_id: int, gastos_variaveis: GastoVariavelPatch):
    with Session(engine) as session:
        gasto_variavel = session.get(GastoVariavel, gasto_variavel_id)
        if not gasto_variavel:
            raise HTTPException(status_code=404, detail="Gasto variável não encontrado")
        
        for key, value in gastos_variaveis.model_dump(exclude_unset=True).items():
            setattr(gasto_variavel, key, value)
        
        session.add(gasto_variavel)
        session.commit()
        session.refresh(gasto_variavel)
        return {"message": "Gasto variável atualizado com sucesso", "data": gasto_variavel}

# Rota para atualizar um proprietário
@app.patch("/proprietarios/{proprietario_id}", response_model=Proprietario)
def patch_proprietario(proprietario_id: str, proprietarios: ProprietarioPatch):
    with Session(engine) as session:
        proprietario = session.get(Proprietario, proprietario_id)
        if not proprietario:
            raise HTTPException(status_code=404, detail="Proprietário não encontrado")
        
        for key, value in proprietarios.model_dump(exclude_unset=True).items():
            setattr(proprietario, key, value)
        
        session.add(proprietario)
        session.commit()
        session.refresh(proprietario)
        return {"message": "Proprietário atualizado com sucesso", "data": proprietario}
