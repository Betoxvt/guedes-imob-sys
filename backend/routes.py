from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db, SessionLocal
from schemas import (
    AluguelCreate, AluguelResponse, AluguelUpdate,
    ApartamentoCreate, ApartamentoResponse, ApartamentoUpdate,
    DespesaCreate, DespesaResponse, DespesaUpdate,
    EdificioCreate, EdificioResponse, EdificioUpdate,
    GaragemCreate, GaragemResponse, GaragemUpdate,
    GastoCreate, GastoResponse, GastoUpdate,
    ProprietarioCreate, ProprietarioResponse, ProprietarioUpdate
)
from crud import (
    create_aluguel, get_aluguel, get_alugueis, update_aluguel, delete_aluguel,
    create_apartamento, get_apartamento, get_apartamentos, update_apartamento, delete_apartamento,
    create_despesa, get_despesa, get_despesas, update_despesa, delete_despesa,
    create_edificio, get_edificio, get_edificios, update_edificio, delete_edificio,
    create_garagem, get_garagem, get_garagens, update_garagem, delete_garagem,
    create_gasto, get_gasto, get_gastos, update_gasto, delete_gasto,
    create_proprietario, get_proprietario, get_proprietarios, update_proprietario, delete_proprietario
)

router = APIRouter()

@router.post("/alugueis", response_model=AluguelResponse)
def create_aluguel_route(aluguel: AluguelCreate, db: Session = Depends(get_db)):
    return create_aluguel(db=db, aluguel=aluguel)


@router.get("/alugueis", response_model=List[AluguelResponse])
def read_alugueis_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alugueis = get_alugueis(db, skip=skip, limit=limit)
    return alugueis


@router.get("/alugueis/{aluguel_id}", response_model=AluguelResponse)
def read_aluguel_route(aluguel_id: int, db: Session = Depends(get_db)):
    aluguel = get_aluguel(db, aluguel_id=aluguel_id)
    if aluguel is None:
        raise HTTPException(status_code=404, detail="Aluguel not found")
    return aluguel


@router.put("/alugueis/{aluguel_id}", response_model=AluguelResponse)
def update_aluguel_route(aluguel_id: int, aluguel: AluguelUpdate, db: Session = Depends(get_db)):
    db_aluguel = update_aluguel(db=db, aluguel_id=aluguel_id, aluguel=aluguel)
    if db_aluguel is None:
        raise HTTPException(status_code=404, detail="Aluguel not found")
    return db_aluguel


@router.delete("/alugueis/{aluguel_id}", response_model=AluguelResponse)
def delete_aluguel_route(aluguel_id: int, db: Session = Depends(get_db)):
    db_aluguel = delete_aluguel(db, aluguel_id=aluguel_id)
    if db_aluguel is None:
        raise HTTPException(status_code=404, detail="Aluguel not found")
    return db_aluguel


@router.post("/apartamentos", response_model=ApartamentoResponse)
def create_apartamento_route(apartamento: ApartamentoCreate, db: Session = Depends(get_db)):
    return create_apartamento(db=db, apartamento=apartamento)


@router.get("/apartamentos", response_model=List[ApartamentoResponse])
def read_apartamentos_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    apartamentos = get_apartamentos(db, skip=skip, limit=limit)
    return apartamentos


@router.get("/apartamentos/{apartamento_id}", response_model=ApartamentoResponse)
def read_apartamento_route(apartamento_id: int, db: Session = Depends(get_db)):
    apartamento = get_apartamento(db, apartamento_id=apartamento_id)
    if apartamento is None:
        raise HTTPException(status_code=404, detail="Apartamento not found")
    return apartamento


@router.put("/apartamentos/{apartamento_id}", response_model=ApartamentoResponse)
def update_apartamento_route(apartamento_id: int, apartamento: ApartamentoUpdate, db: Session = Depends(get_db)):
    db_apartamento = update_apartamento(db=db, apartamento_id=apartamento_id, apartamento=apartamento)
    if db_apartamento is None:
        raise HTTPException(status_code=404, detail="Apartamento not found")
    return db_apartamento


@router.delete("/apartamentos/{apartamento_id}", response_model=ApartamentoResponse)
def delete_apartamento_route(apartamento_id: int, db: Session = Depends(get_db)):
    db_apartamento = delete_apartamento(db, apartamento_id=apartamento_id)
    if db_apartamento is None:
        raise HTTPException(status_code=404, detail="Apartamento not found")
    return db_apartamento


@router.post("/despesas", response_model=DespesaResponse)
def create_despesa_route(despesa: DespesaCreate, db: Session = Depends(get_db)):
    return create_despesa(db=db, despesa=despesa)


@router.get("/despesas", response_model=List[DespesaResponse])
def read_despesas_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    despesas = get_despesas(db, skip=skip, limit=limit)
    return despesas


@router.get("/despesas/{despesa_id}", response_model=DespesaResponse)
def read_despesa_route(despesa_id: int, db: Session = Depends(get_db)):
    despesa = get_despesa(db, despesa_id=despesa_id)
    if despesa is None:
        raise HTTPException(status_code=404, detail="Despesa not found")
    return despesa


@router.put("/despesas/{despesa_id}", response_model=DespesaResponse)
def update_despesa_route(despesa_id: int, despesa: DespesaUpdate, db: Session = Depends(get_db)):
    db_despesa = update_despesa(db=db, despesa_id=despesa_id, despesa=despesa)
    if db_despesa is None:
        raise HTTPException(status_code=404, detail="Despesa not found")
    return db_despesa


@router.delete("/despesas/{despesa_id}", response_model=DespesaResponse)
def delete_despesa_route(despesa_id: int, db: Session = Depends(get_db)):
    db_despesa = delete_despesa(db, despesa_id=despesa_id)
    if db_despesa is None:
        raise HTTPException(status_code=404, detail="Despesa not found")
    return db_despesa


@router.post("/edificios", response_model=EdificioResponse)
def create_edificio_route(edificio: EdificioCreate, db: Session = Depends(get_db)):
    return create_edificio(db=db, edificio=edificio)


@router.get("/edificios", response_model=List[EdificioResponse])
def read_edificios_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    edificios = get_edificios(db, skip=skip, limit=limit)
    return edificios


@router.get("/edificios/{edificio_id}", response_model=EdificioResponse)
def read_edificio_route(edificio_id: int, db: Session = Depends(get_db)):
    edificio = get_edificio(db, edificio_id=edificio_id)
    if edificio is None:
        raise HTTPException(status_code=404, detail="Edificio not found")
    return edificio


@router.put("/edificios/{edificio_id}", response_model=EdificioResponse)
def update_edificio_route(edificio_id: int, edificio: EdificioUpdate, db: Session = Depends(get_db)):
    db_edificio = update_edificio(db=db, edificio_id=edificio_id, edificio=edificio)
    if db_edificio is None:
        raise HTTPException(status_code=404, detail="Edificio not found")
    return db_edificio


@router.delete("/edificios/{edificio_id}", response_model=EdificioResponse)
def delete_edificio_route(edificio_id: int, db: Session = Depends(get_db)):
    db_edificio = delete_edificio(db, edificio_id=edificio_id)
    if db_edificio is None:
        raise HTTPException(status_code=404, detail="Edificio not found")
    return db_edificio


@router.post("/garagens", response_model=GaragemResponse)
def create_garagem_route(garagem: GaragemCreate, db: Session = Depends(get_db)):
    return create_garagem(db=db, garagem=garagem)


@router.get("/garagens", response_model=List[GaragemResponse])
def read_garagens_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    garagens = get_garagens(db, skip=skip, limit=limit)
    return garagens


@router.get("/garagens/{garagem_id}", response_model=GaragemResponse)
def read_garagem_route(garagem_id: int, db: Session = Depends(get_db)):
    garagem = get_garagem(db, garagem_id=garagem_id)
    if garagem is None:
        raise HTTPException(status_code=404, detail="Garagem not found")
    return garagem


@router.put("/garagens/{garagem_id}", response_model=GaragemResponse)
def update_garagem_route(garagem_id: int, garagem: GaragemUpdate, db: Session = Depends(get_db)):
    db_garagem = update_garagem(db=db, garagem_id=garagem_id, garagem=garagem)
    if db_garagem is None:
        raise HTTPException(status_code=404, detail="Garagem not found")
    return db_garagem


@router.delete("/garagens/{garagem_id}", response_model=GaragemResponse)
def delete_garagem_route(garagem_id: int, db: Session = Depends(get_db)):
    db_garagem = delete_garagem(db, garagem_id=garagem_id)
    if db_garagem is None:
        raise HTTPException(status_code=404, detail="Garagem not found")
    return db_garagem


@router.post("/gastos", response_model=GastoResponse)
def create_gasto_route(gasto: GastoCreate, db: Session = Depends(get_db)):
    return create_gasto(db=db, gasto=gasto)


@router.get("/gastos", response_model=List[GastoResponse])
def read_gastos_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gastos = get_gastos(db, skip=skip, limit=limit)
    return gastos


@router.get("/gastos/{gasto_id}", response_model=GastoResponse)
def read_gasto_route(gasto_id: int, db: Session = Depends(get_db)):
    gasto = get_gasto(db, gasto_id=gasto_id)
    if gasto is None:
        raise HTTPException(status_code=404, detail="Gasto not found")
    return gasto


@router.put("/gastos/{gasto_id}", response_model=GastoResponse)
def update_gasto_route(gasto_id: int, gasto: GastoUpdate, db: Session = Depends(get_db)):
    db_gasto = update_gasto(db=db, gasto_id=gasto_id, gasto=gasto)
    if db_gasto is None:
        raise HTTPException(status_code=404, detail="Gasto not found")
    return db_gasto


@router.delete("/gastos/{gasto_id}", response_model=GastoResponse)
def delete_gasto_route(gasto_id: int, db: Session = Depends(get_db)):
    db_gasto = delete_gasto(db, gasto_id=gasto_id)
    if db_gasto is None:
        raise HTTPException(status_code=404, detail="Gasto not found")
    return db_gasto


@router.post("/proprietarios", response_model=ProprietarioResponse)
def create_proprietario_route(proprietario: ProprietarioCreate, db: Session = Depends(get_db)):
    return create_proprietario(db=db, proprietario=proprietario)


@router.get("/proprietarios", response_model=List[ProprietarioResponse])
def read_proprietarios_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    proprietarios = get_proprietarios(db, skip=skip, limit=limit)
    return proprietarios


@router.get("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def read_proprietario_route(proprietario_id: int, db: Session = Depends(get_db)):
    proprietario = get_proprietario(db, proprietario_id=proprietario_id)
    if proprietario is None:
        raise HTTPException(status_code=404, detail="Proprietario not found")
    return proprietario


@router.put("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def update_proprietario_route(proprietario_id: int, proprietario: ProprietarioUpdate, db: Session = Depends(get_db)):
    db_proprietario = update_proprietario(db=db, proprietario_id=proprietario_id, proprietario=proprietario)
    if db_proprietario is None:
        raise HTTPException(status_code=404, detail="Proprietario not found")
    return db_proprietario


@router.delete("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def delete_proprietario_route(proprietario_id: int, db: Session = Depends(get_db)):
    db_proprietario = delete_proprietario(db, proprietario_id=proprietario_id)
    if db_proprietario is None:
        raise HTTPException(status_code=404, detail="Proprietario not found")
    return db_proprietario
