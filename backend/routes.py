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
