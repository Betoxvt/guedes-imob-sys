from crud import (
    create_aluguel,
    read_alugueis,
    read_aluguel,
    update_aluguel,
    patch_aluguel,
    delete_aluguel,
    create_apartamento,
    read_apartamentos,
    read_apartamento,
    update_apartamento,
    patch_apartamento,
    delete_apartamento,
    create_despesa,
    read_despesas,
    read_despesa,
    update_despesa,
    patch_despesa,
    delete_despesa,
    create_ficha,
    read_ficha,
    read_fichas,
    update_ficha,
    patch_ficha,
    delete_ficha,
    create_garagem,
    read_garagem,
    read_garagens,
    update_garagem,
    patch_garagem,
    delete_garagem,
    create_pagamento,
    read_pagamento,
    read_pagamentos,
    update_pagamento,
    patch_pagamento,
    delete_pagamento,
    create_proprietario,
    read_proprietario,
    read_proprietarios,
    update_proprietario,
    patch_proprietario,
    delete_proprietario,
    create_relatorio,
    read_relatorio,
    read_relatorios,
    update_relatorio,
    patch_relatorio,
    delete_relatorio,
)
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import (
    AluguelCreate,
    AluguelResponse,
    AluguelUpdate,
    ApartamentoCreate,
    ApartamentoResponse,
    ApartamentoUpdate,
    DespesaCreate,
    DespesaResponse,
    DespesaUpdate,
    FichaCreate,
    FichaResponse,
    FichaUpdate,
    GaragemCreate,
    GaragemResponse,
    GaragemUpdate,
    PagamentoCreate,
    PagamentoResponse,
    PagamentoUpdate,
    ProprietarioCreate,
    ProprietarioResponse,
    ProprietarioUpdate,
    RelatorioCreate,
    RelatorioResponse,
    RelatorioUpdate,
)
from typing import List

router = APIRouter()


@router.post("/alugueis/", response_model=AluguelResponse)
def create_aluguel_route(aluguel: AluguelCreate, db: Session = Depends(get_db)):
    return create_aluguel(db=db, aluguel=aluguel)


@router.get("/alugueis/", response_model=List[AluguelResponse])
def read_alugueis_route(
    db: Session = Depends(get_db),
    apto_id: str | None = None,
    checkin: str | None = None,
    offset: int = 0,
    limit: int = 100,
):
    alugueis = read_alugueis(
        db, apto_id=apto_id, checkin=checkin, offset=offset, limit=limit
    )
    return alugueis


@router.get("/alugueis/{aluguel_id}", response_model=AluguelResponse)
def read_aluguel_route(aluguel_id: int, db: Session = Depends(get_db)):
    aluguel = read_aluguel(db, aluguel_id=aluguel_id)
    if aluguel is None:
        raise HTTPException(status_code=404, detail="Aluguel not found")
    return aluguel


@router.put("/alugueis/{aluguel_id}", response_model=AluguelResponse)
def update_aluguel_route(
    aluguel_id: int, aluguel: AluguelCreate, db: Session = Depends(get_db)
):
    db_aluguel = update_aluguel(db=db, aluguel_id=aluguel_id, aluguel=aluguel)
    if db_aluguel is None:
        raise HTTPException(status_code=404, detail="Aluguel not found")
    return db_aluguel


@router.patch("/alugueis/{aluguel_id}", response_model=AluguelUpdate)
def patch_aluguel_route(
    aluguel_id: int, aluguel: AluguelUpdate, db: Session = Depends(get_db)
):
    db_aluguel = patch_aluguel(db=db, aluguel_id=aluguel_id, aluguel=aluguel)
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
def create_apartamento_route(
    apartamento: ApartamentoCreate, db: Session = Depends(get_db)
):
    return create_apartamento(db=db, apartamento=apartamento)


@router.get("/apartamentos/", response_model=List[ApartamentoResponse])
def read_apartamentos_route(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    apartamentos = read_apartamentos(db, offset=offset, limit=limit)
    return apartamentos


@router.get("/apartamentos/{apartamento_id}", response_model=ApartamentoResponse)
def read_apartamento_route(apartamento_id: str, db: Session = Depends(get_db)):
    apartamento = read_apartamento(db, apartamento_id=apartamento_id)
    if apartamento is None:
        raise HTTPException(status_code=404, detail="Apartamento not found")
    return apartamento


@router.put("/apartamentos/{apartamento_id}", response_model=ApartamentoResponse)
def update_apartamento_route(
    apartamento_id: str, apartamento: ApartamentoCreate, db: Session = Depends(get_db)
):
    db_apartamento = update_apartamento(
        db=db, apartamento_id=apartamento_id, apartamento=apartamento
    )
    if db_apartamento is None:
        raise HTTPException(status_code=404, detail="Apartamento not found")
    return db_apartamento


@router.patch("/apartamentos/{apartamento_id}", response_model=ApartamentoResponse)
def patch_apartamento_route(
    apartamento_id: str, apartamento: ApartamentoUpdate, db: Session = Depends(get_db)
):
    db_apartamento = patch_apartamento(
        db=db, apartamento_id=apartamento_id, apartamento=apartamento
    )
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
def read_despesas_route(
    db: Session = Depends(get_db),
    apto_id: str | None = None,
    offset: int = 0,
    limit: int = 100,
):
    despesas = read_despesas(db, apto_id=apto_id, offset=offset, limit=limit)
    return despesas


@router.get("/despesas/{despesa_id}", response_model=DespesaResponse)
def read_despesa_route(despesa_id: int, db: Session = Depends(get_db)):
    despesa = read_despesa(db, despesa_id=despesa_id)
    if despesa is None:
        raise HTTPException(status_code=404, detail="Despesa not found")
    return despesa


@router.put("/despesas/{despesa_id}", response_model=DespesaResponse)
def update_despesa_route(
    despesa_id: int, despesa: DespesaCreate, db: Session = Depends(get_db)
):
    db_despesa = update_despesa(db=db, despesa_id=despesa_id, despesa=despesa)
    if db_despesa is None:
        raise HTTPException(status_code=404, detail="Despesa not found")
    return db_despesa


@router.patch("/despesas/{despesa_id}", response_model=DespesaResponse)
def patch_despesa_route(
    despesa_id: int, despesa: DespesaUpdate, db: Session = Depends(get_db)
):
    db_despesa = patch_despesa(db=db, despesa_id=despesa_id, despesa=despesa)
    if db_despesa is None:
        raise HTTPException(status_code=404, detail="Despesa not found")
    return db_despesa


@router.delete("/despesas/{despesa_id}", response_model=DespesaResponse)
def delete_despesa_route(despesa_id: int, db: Session = Depends(get_db)):
    db_despesa = delete_despesa(db, despesa_id=despesa_id)
    if db_despesa is None:
        raise HTTPException(status_code=404, detail="Despesa not found")
    return db_despesa


@router.post("/garagens/", response_model=GaragemResponse)
def create_garagem_route(garagem: GaragemCreate, db: Session = Depends(get_db)):
    return create_garagem(db=db, garagem=garagem)


@router.get("/garagens/", response_model=List[GaragemResponse])
def read_garagens_route(
    db: Session = Depends(get_db),
    apto_id_origem: str | None = None,
    apto_id_destino: str | None = None,
    offset: int = 0,
    limit: int = 100,
):
    garagens = read_garagens(
        db,
        apto_id_origem=apto_id_origem,
        apto_id_destino=apto_id_destino,
        offset=offset,
        limit=limit,
    )
    return garagens


@router.get("/garagens/{garagem_id}", response_model=GaragemResponse)
def read_garagem_route(garagem_id: int, db: Session = Depends(get_db)):
    garagem = read_garagem(db, garagem_id=garagem_id)
    if garagem is None:
        raise HTTPException(status_code=404, detail="Garagem not found")
    return garagem


@router.put("/garagens/{garagem_id}", response_model=GaragemResponse)
def update_garagem_route(
    garagem_id: int, garagem: GaragemCreate, db: Session = Depends(get_db)
):
    db_garagem = update_garagem(db=db, garagem_id=garagem_id, garagem=garagem)
    if db_garagem is None:
        raise HTTPException(status_code=404, detail="Garagem not found")
    return db_garagem


@router.patch("/garagens/{garagem_id}", response_model=GaragemResponse)
def patch_garagem_route(
    garagem_id: int, garagem: GaragemUpdate, db: Session = Depends(get_db)
):
    db_garagem = patch_garagem(db=db, garagem_id=garagem_id, garagem=garagem)
    if db_garagem is None:
        raise HTTPException(status_code=404, detail="Garagem not found")
    return db_garagem


@router.delete("/garagens/{garagem_id}", response_model=GaragemResponse)
def delete_garagem_route(garagem_id: int, db: Session = Depends(get_db)):
    db_garagem = delete_garagem(db, garagem_id=garagem_id)
    if db_garagem is None:
        raise HTTPException(status_code=404, detail="Garagem not found")
    return db_garagem


@router.post("/proprietarios/", response_model=ProprietarioResponse)
def create_proprietario_route(
    proprietario: ProprietarioCreate, db: Session = Depends(get_db)
):
    return create_proprietario(db=db, proprietario=proprietario)


@router.get("/proprietarios/", response_model=List[ProprietarioResponse])
def read_proprietarios_route(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    proprietarios = read_proprietarios(db, offset=offset, limit=limit)
    return proprietarios


@router.get("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def read_proprietario_route(proprietario_id: int, db: Session = Depends(get_db)):
    proprietario = read_proprietario(db, proprietario_id=proprietario_id)
    if proprietario is None:
        raise HTTPException(status_code=404, detail="Proprietario not found")
    return proprietario


@router.put("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def update_proprietario_route(
    proprietario_id: int,
    proprietario: ProprietarioCreate,
    db: Session = Depends(get_db),
):
    db_proprietario = update_proprietario(
        db=db, proprietario_id=proprietario_id, proprietario=proprietario
    )
    if db_proprietario is None:
        raise HTTPException(status_code=404, detail="Proprietario not found")
    return db_proprietario


@router.patch("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def patch_proprietario_route(
    proprietario_id: int,
    proprietario: ProprietarioUpdate,
    db: Session = Depends(get_db),
):
    db_proprietario = patch_proprietario(
        db=db, proprietario_id=proprietario_id, proprietario=proprietario
    )
    if db_proprietario is None:
        raise HTTPException(status_code=404, detail="Proprietario not found")
    return db_proprietario


@router.delete("/proprietarios/{proprietario_id}", response_model=ProprietarioResponse)
def delete_proprietario_route(proprietario_id: int, db: Session = Depends(get_db)):
    db_proprietario = delete_proprietario(db, proprietario_id=proprietario_id)
    if db_proprietario is None:
        raise HTTPException(status_code=404, detail="Proprietario not found")
    return db_proprietario


@router.post("/fichas/", response_model=FichaResponse)
def create_ficha_route(ficha: FichaCreate, db: Session = Depends(get_db)):
    return create_ficha(db=db, ficha=ficha)


@router.get("/fichas/", response_model=List[FichaResponse])
def read_fichas_route(
    db: Session = Depends(get_db),
    aluguel_id: int | None = None,
    apto_id: str | None = None,
    checkin: str | None = None,
    offset: int = 0,
    limit: int = 100,
):
    fichas = read_fichas(
        db,
        aluguel_id=aluguel_id,
        apto_id=apto_id,
        checkin=checkin,
        offset=offset,
        limit=limit,
    )
    return fichas


@router.get("/fichas/{ficha_id}", response_model=FichaResponse)
def read_ficha_route(ficha_id: int, db: Session = Depends(get_db)):
    ficha = read_ficha(db, ficha_id=ficha_id)
    if ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    return ficha


@router.put("/fichas/{ficha_id}", response_model=FichaResponse)
def update_ficha_route(
    ficha_id: int, ficha: FichaCreate, db: Session = Depends(get_db)
):
    db_ficha = update_ficha(db=db, ficha_id=ficha_id, ficha=ficha)
    if db_ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    return db_ficha


@router.patch("/fichas/{ficha_id}", response_model=FichaResponse)
def patch_ficha_route(ficha_id: int, ficha: FichaUpdate, db: Session = Depends(get_db)):
    db_ficha = patch_ficha(db=db, ficha_id=ficha_id, ficha=ficha)
    if db_ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    return db_ficha


@router.delete("/fichas/{ficha_id}", response_model=FichaResponse)
def delete_ficha_route(ficha_id: int, db: Session = Depends(get_db)):
    db_ficha = delete_ficha(db, ficha_id=ficha_id)
    if db_ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    return db_ficha


@router.post("/pagamentos/", response_model=PagamentoResponse)
def create_pagamento_route(pagamento: PagamentoCreate, db: Session = Depends(get_db)):
    return create_pagamento(db=db, pagamento=pagamento)


@router.get("/pagamentos/", response_model=List[PagamentoResponse])
def read_pagamentos_route(
    db: Session = Depends(get_db),
    aluguel_id: int | None = None,
    tipo: str | None = None,
    offset: int = 0,
    limit: int = 100,
):
    pagamentos = read_pagamentos(
        db, aluguel_id=aluguel_id, tipo=tipo, offset=offset, limit=limit
    )
    return pagamentos


@router.get("/pagamentos/{pagamento_id}", response_model=PagamentoResponse)
def read_pagamento_route(pagamento_id: int, db: Session = Depends(get_db)):
    pagamento = read_pagamento(db, pagamento_id=pagamento_id)
    if pagamento is None:
        raise HTTPException(status_code=404, detail="Pagamento not found")
    return pagamento


@router.put("/pagamentos/{pagamento_id}", response_model=PagamentoResponse)
def update_pagamento_route(
    pagamento_id: int, pagamento: PagamentoCreate, db: Session = Depends(get_db)
):
    db_pagamento = update_pagamento(
        db=db, pagamento_id=pagamento_id, pagamento=pagamento
    )
    if db_pagamento is None:
        raise HTTPException(status_code=404, detail="Pagamento not found")
    return db_pagamento


@router.patch("/pagamentos/{pagamento_id}", response_model=PagamentoResponse)
def patch_pagamento_route(
    pagamento_id: int, pagamento: PagamentoUpdate, db: Session = Depends(get_db)
):
    db_pagamento = patch_pagamento(
        db=db, pagamento_id=pagamento_id, pagamento=pagamento
    )
    if db_pagamento is None:
        raise HTTPException(status_code=404, detail="Pagamento not found")
    return db_pagamento


@router.delete("/pagamentos/{pagamento_id}", response_model=PagamentoResponse)
def delete_pagamento_route(pagamento_id: int, db: Session = Depends(get_db)):
    db_pagamento = delete_pagamento(db, pagamento_id=pagamento_id)
    if db_pagamento is None:
        raise HTTPException(status_code=404, detail="Pagamento not found")
    return db_pagamento


@router.post("/relatorios/", response_model=RelatorioResponse)
def create_relatorio_route(relatorio: RelatorioCreate, db: Session = Depends(get_db)):
    return create_relatorio(db=db, relatorio=relatorio)


@router.get("/relatorios/", response_model=List[RelatorioResponse])
def read_relatorios_route(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    relatorios = read_relatorios(db, offset=offset, limit=limit)
    return relatorios


@router.get("/relatorios/{relatorio_id}", response_model=RelatorioResponse)
def read_relatorio_route(relatorio_id: int, db: Session = Depends(get_db)):
    relatorio = read_relatorio(db, relatorio_id=relatorio_id)
    if relatorio is None:
        raise HTTPException(status_code=404, detail="Relatorio not found")
    return relatorio


@router.put("/relatorios/{relatorio_id}", response_model=RelatorioResponse)
def update_relatorio_route(
    relatorio_id: int, relatorio: RelatorioCreate, db: Session = Depends(get_db)
):
    db_relatorio = update_relatorio(
        db=db, relatorio_id=relatorio_id, relatorio=relatorio
    )
    if db_relatorio is None:
        raise HTTPException(status_code=404, detail="Relatorio not found")
    return db_relatorio


@router.patch("/relatorios/{relatorio_id}", response_model=RelatorioUpdate)
def patch_relatorio_route(
    relatorio_id: int, relatorio: RelatorioUpdate, db: Session = Depends(get_db)
):
    db_relatorio = patch_relatorio(
        db=db, relatorio_id=relatorio_id, relatorio=relatorio
    )
    if db_relatorio is None:
        raise HTTPException(status_code=404, detail="Relatorio not found")
    return db_relatorio


@router.delete("/relatorios/{relatorio_id}", response_model=RelatorioResponse)
def delete_relatorio_route(relatorio_id: int, db: Session = Depends(get_db)):
    db_relatorio = delete_relatorio(db, relatorio_id=relatorio_id)
    if db_relatorio is None:
        raise HTTPException(status_code=404, detail="Relatorio not found")
    return db_relatorio
