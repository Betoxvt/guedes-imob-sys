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
    ProprietarioCreate, ProprietarioResponse, ProprietarioUpdate,
    InquilinoCreate, InquilinoResponse, InquilinoUpdate
)
from crud import (
    create_aluguel, read_alugueis, read_aluguel, update_aluguel, delete_aluguel,
    create_apartamento, read_apartamentos, read_apartamento, update_apartamento, delete_apartamento,
    create_despesa, read_despesas, read_despesa, update_despesa, delete_despesa,
    create_edificio, read_edificio, read_edificios, update_edificio, delete_edificio,
    create_garagem, read_garagem, read_garagens, update_garagem, delete_garagem,
    create_gasto, read_gasto, read_gastos, update_gasto, delete_gasto,
    create_proprietario, read_proprietario, read_proprietarios, update_proprietario, delete_proprietario,
    create_inquilino, read_inquilino, read_inquilinos, update_inquilino, delete_inquilino
)

router = APIRouter()

@router.post("/alugueis/", response_model=AluguelResponse)
def create_aluguel_route(aluguel: AluguelCreate, db: Session = Depends(get_db)):
    return create_aluguel(db=db, aluguel=aluguel)


@router.get("/alugueis/", response_model=List[AluguelResponse])
def read_alugueis_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alugueis = read_alugueis(db, offset=offset, limit=limit)
    return alugueis


@router.get("/alugueis/{aluguel_id}", response_model=AluguelResponse)
def read_aluguel_route(aluguel_id: int, db: Session = Depends(get_db)):
    aluguel = read_aluguel(db, aluguel_id=aluguel_id)
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


@router.post("/apartamentos/", response_model=ApartamentoResponse)
def create_apartamento_route(apartamento: ApartamentoCreate, db: Session = Depends(get_db)):
    return create_apartamento(db=db, apartamento=apartamento)


@router.get("/apartamentos/", response_model=List[ApartamentoResponse])
def read_apartamentos_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    apartamentos = read_apartamentos(db, offset=offset, limit=limit)
    return apartamentos


@router.get("/apartamentos/{apartamento_id}", response_model=ApartamentoResponse)
def read_apartamento_route(apartamento_id: int, db: Session = Depends(get_db)):
    apartamento = read_apartamento(db, apartamento_id=apartamento_id)
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


@router.post("/despesas/", response_model=DespesaResponse)
def create_despesa_route(despesa: DespesaCreate, db: Session = Depends(get_db)):
    return create_despesa(db=db, despesa=despesa)


@router.get("/despesas/", response_model=List[DespesaResponse])
def read_despesas_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    despesas = read_despesas(db, offset=offset, limit=limit)
    return despesas


@router.get("/despesas/{despesa_id}", response_model=DespesaResponse)
def read_despesa_route(despesa_id: int, db: Session = Depends(get_db)):
    despesa = read_despesa(db, despesa_id=despesa_id)
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


@router.post("/edificios/", response_model=EdificioResponse)
def create_edificio_route(edificio: EdificioCreate, db: Session = Depends(get_db)):
    return create_edificio(db=db, edificio=edificio)


@router.get("/edificios/", response_model=List[EdificioResponse])
def read_edificios_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    edificios = read_edificios(db, offset=offset, limit=limit)
    return edificios


@router.get("/edificios/{edificio_id}", response_model=EdificioResponse)
def read_edificio_route(edificio_id: int, db: Session = Depends(get_db)):
    edificio = read_edificio(db, edificio_id=edificio_id)
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


@router.post("/garagens/", response_model=GaragemResponse)
def create_garagem_route(garagem: GaragemCreate, db: Session = Depends(get_db)):
    return create_garagem(db=db, garagem=garagem)


@router.get("/garagens/", response_model=List[GaragemResponse])
def read_garagens_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    garagens = read_garagens(db, offset=offset, limit=limit)
    return garagens


@router.get("/garagens/{garagem_id}", response_model=GaragemResponse)
def read_garagem_route(garagem_id: int, db: Session = Depends(get_db)):
    garagem = read_garagem(db, garagem_id=garagem_id)
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


@router.post("/gastos/", response_model=GastoResponse)
def create_gasto_route(gasto: GastoCreate, db: Session = Depends(get_db)):
    return create_gasto(db=db, gasto=gasto)


@router.get("/gastos/", response_model=List[GastoResponse])
def read_gastos_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gastos = read_gastos(db, offset=offset, limit=limit)
    return gastos


@router.get("/gastos/{gasto_id}", response_model=GastoResponse)
def read_gasto_route(gasto_id: int, db: Session = Depends(get_db)):
    gasto = read_gasto(db, gasto_id=gasto_id)
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


@router.post("/proprietarios/", response_model=ProprietarioResponse)
def create_proprietario_route(proprietario: ProprietarioCreate, db: Session = Depends(get_db)):
    return create_proprietario(db=db, proprietario=proprietario)


@router.get("/proprietarios", response_model=List[ProprietarioResponse])
def read_proprietarios_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    proprietarios = read_proprietarios(db, offset=offset, limit=limit)
    return proprietarios


@router.get("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def read_proprietario_route(proprietario_id: int, db: Session = Depends(get_db)):
    proprietario = read_proprietario(db, proprietario_id=proprietario_id)
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


@router.post("/inquilinos/", response_model=InquilinoResponse)
def create_inquilino_route(inquilino: InquilinoCreate, db: Session = Depends(get_db)):
    return create_inquilino(db=db, inquilino=inquilino)


@router.get("/inquilinos/", response_model=List[InquilinoResponse])
def read_inquilinos_route(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    inquilinos = read_inquilinos(db, offset=offset, limit=limit)
    return inquilinos


@router.get("/inquilinos/{inquilino_id}", response_model=InquilinoResponse)
def read_inquilino_route(inquilino_id: int, db: Session = Depends(get_db)):
    inquilino = read_inquilino(db, inquilino_id=inquilino_id)
    if inquilino is None:
        raise HTTPException(status_code=404, detail="Inquilino not found")
    return inquilino


@router.put("/inquilinos/{inquilino_id}", response_model=InquilinoResponse)
def update_inquilino_route(inquilino_id: int, inquilino: InquilinoUpdate, db: Session = Depends(get_db)):
    db_inquilino = update_inquilino(db=db, inquilino_id=inquilino_id, inquilino=inquilino)
    if db_inquilino is None:
        raise HTTPException(status_code=404, detail="Inquilino not found")
    return db_inquilino


@router.delete("/inquilinos/{inquilino_id}", response_model=InquilinoResponse)
def delete_inquilino_route(inquilino_id: int, db: Session = Depends(get_db)):
    db_inquilino = delete_inquilino(db, inquilino_id=inquilino_id)
    if db_inquilino is None:
        raise HTTPException(status_code=404, detail="Inquilino not found")
    return db_inquilino
