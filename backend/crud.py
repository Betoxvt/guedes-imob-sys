from sqlalchemy.orm import Session
from schemas import (
    AluguelCreate, AluguelUpdate,
    ApartamentoCreate, ApartamentoUpdate,
    DespesaCreate, DespesaUpdate,
    GaragemCreate, GaragemUpdate,
    EdificioCreate, EdificioUpdate,
    GastoCreate, GastoUpdate,
    ProprietarioCreate, ProprietarioUpdate
)
from models import (
    Aluguel, Apartamento, Despesa, Edificio, Garagem, Gasto, Proprietario
)


def create_aluguel(db: Session, aluguel: AluguelCreate):
    """
    Creates a new element in the database table alugueis
    """
    db_aluguel = Aluguel(**aluguel.model_dump())
    db.add(db_aluguel)
    db.commit()
    db.refresh(db_aluguel)
    return db_aluguel


def get_alugueis(db: Session, skip: int = 0, limit: int = 100):
    """
    Returns all elements from the database table alugueis
    """
    return db.query(Aluguel).order_by(Aluguel.id.desc()).offset(skip).limit(limit).all()


def get_aluguel(db: Session, aluguel_id: int):
    """
    Returns a specific element from the database table alugueis
    """
    return db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()


def update_aluguel(db: Session, aluguel_id: int, aluguel: AluguelUpdate):
    """
    Updates a specific element from the database table alugueis
    """
    db_aluguel = db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()

    if db_aluguel is None:
        return None
    
    if aluguel.apartamento_id is not None:
        db_aluguel.apartamento_id = aluguel.apartamento_id
    if aluguel.checkin is not None:
        db_aluguel.checkin = aluguel.checkin
    if aluguel.checkout is not None:
        db_aluguel.checkout = aluguel.checkout
    if aluguel.diarias is not None:
        db_aluguel.diarias = aluguel.diarias
    if aluguel.valor_diaria is not None:
        db_aluguel.valor_diaria = aluguel.valor_diaria
    if aluguel.taxa_adm is not None:
        db_aluguel.taxa_adm = aluguel.taxa_adm
    if aluguel.valor_total is not None:
        db_aluguel.valor_total = aluguel.valor_total
    if aluguel.valor_imob is not None:
        db_aluguel.valor_imob = aluguel.valor_imob
    if aluguel.valor_prop is not None:
        db_aluguel.valor_prop = aluguel.valor_prop
    
    db.commit()
    db.refresh(db_aluguel)
    return db_aluguel


def delete_aluguel(db: Session, aluguel_id: int):
    """
    Deletes a specific element from the database table alugueis
    """
    db_aluguel = db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
    db.delete(db_aluguel)
    db.commit()
    return db_aluguel


def create_apartamento(db: Session, apartamento: ApartamentoCreate):
    """
    Creates a new element in the database table apartamentos
    """
    db_apartamento = Apartamento(**apartamento.model_dump())
    db.add(db_apartamento)
    db.commit()
    db.refresh(db_apartamento)
    return db_apartamento


def get_apartamentos(db: Session, skip: int = 0, limit: int = 100):

    """
    Returns all elements from the database table apartamentos
    """
    return db.query(Apartamento).offset(skip).limit(limit).all()


def get_apartamento(db: Session, apartamento_id: int):
    """
    Returns a specific element from the database table apartamentos
    """
    return db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()


def update_apartamento(db: Session, apartamento_id: int, apartamento: ApartamentoUpdate):
    """
    Updates a specific element from the database table apartamentos
    """
    db_apartamento = db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()

    if db_apartamento is None:
        return None
    
    if apartamento.apartamento is not None:
        db_apartamento.apartamento = apartamento.apartamento
    if apartamento.edificio_id is not None:
        db_apartamento.edificio_id = apartamento.edificio_id
    if apartamento.proprietario_id is not None:
        db_apartamento.proprietario_id = apartamento.proprietario_id
    if apartamento.celesc is not None:
        db_apartamento.celesc = apartamento.celesc
    if apartamento.supergasbras is not None:
        db_apartamento.supergasbras = apartamento.supergasbras
    if apartamento.internet_provedor is not None:
        db_apartamento.internet_provedor = apartamento.internet_provedor
    if apartamento.wifiid is not None:
        db_apartamento.wifiid = apartamento.wifiid
    if apartamento.wifipass is not None:
        db_apartamento.wifipass = apartamento.wifipass
    if apartamento.lockpass is not None:
        db_apartamento.lockpass = apartamento.lockpass

    db.commit()
    db.refresh(db_apartamento)
    return db_apartamento


def delete_apartamento(db: Session, apartamento_id: int):
    """
    Deletes a specific element from the database table apartamentos
    """
    db_apartamento = db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
    db.delete(db_apartamento)
    db.commit()
    return db_apartamento


def create_despesa(db: Session, despesa: DespesaCreate):
    """
    Creates a new element in the database table despesas
    """
    db_despesa = Despesa(**despesa.model_dump())
    db.add(db_despesa)
    db.commit()
    db.refresh(db_despesa)
    return db_despesa


def get_despesas(db: Session, skip: int = 0, limit: int = 100):
    """
    Returns all elements from the database table despesas
    """
    return db.query(Despesa).orderby(Despesa.id.desc()).offset(skip).limit(limit).all()


def get_despesa(db: Session, despesa_id: int):
    """
    Returns a specific element from the database table despesas
    """
    return db.query(Despesa).filter(Despesa.id == despesa_id).first()


def update_despesa(db: Session, despesa_id: int, despesa: DespesaUpdate):
    """
    Updates a specific element from the database table despesas
    """
    db_despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()

    if db_despesa is None:
        return None
    
    if despesa.apartamento_id is not None:
        db_despesa.apartamento_id = despesa.apartamento_id
    if despesa.data_pagamento is not None:
        db_despesa.data_pagamento = despesa.data_pagamento
    if despesa.valor is not None:
        db_despesa.valor = despesa.valor
    if despesa.descricao is not None:
        db_despesa.descricao = despesa.descricao
    
    db.commit()
    db.refresh(db_despesa)
    return db_despesa


def delete_despesa(db: Session, despesa_id: int):
    """
    Deletes a specific element from the database table despesas
    """
    db_despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
    db.delete(db_despesa)
    db.commit()
    return db_despesa


def create_edificio(db: Session, edificio: EdificioCreate):
    """
    Creates a new element in the database table edificios
    """
    db_edificio = Edificio(**edificio.model_dump())
    db.add(db_edificio)
    db.commit()
    db.refresh(db_edificio)
    return db_edificio


def get_edificios(db: Session, skip: int = 0, limit: int = 100):
    """
    Returns all elements from the database table edificios
    """
    return db.query(Edificio).offset(skip).limit(limit).all()


def get_edificio(db: Session, edificio_id: int):
    """
    Returns a specific element from the database table edificios
    """
    return db.query(Edificio).filter(Edificio.id == edificio_id).first()


def update_edificio(db: Session, edificio_id: int, edificio: EdificioUpdate):
    """
    Updates a specific element from the database table edificios
    """
    db_edificio = db.query(Edificio).filter(Edificio.id == edificio_id).first()

    if db_edificio is None:
        return None
    
    if edificio.nome is not None:
        db_edificio.nome = edificio.nome
    if edificio.logradouro is not None:
        db_edificio.logradouro = edificio.logradouro
    if edificio.numero is not None:
        db_edificio.numero = edificio.numero
    if edificio.bairro is not None:
        db_edificio.bairro = edificio.bairro
    if edificio.cidade is not None:
        db_edificio.cidade = edificio.cidade
    if edificio.uf is not None:
        db_edificio.uf = edificio.uf
    if edificio.pais is not None:
        db_edificio.pais = edificio.pais
    if edificio.cep is not None:
        db_edificio.cep = edificio.cep
    
    db.commit()
    db.refresh(db_edificio)
    return db_edificio


def delete_edificio(db: Session, edificio_id: int):
    """
    Deletes a specific element from the database table edificios
    """
    db_edificio = db.query(Edificio).filter(Edificio.id == edificio_id).first()
    db.delete(db_edificio)
    db.commit()
    return db_edificio


def create_garagem(db: Session, garagem: GaragemCreate):
    """
    Creates a new element in the database table garagens
    """
    db_garagem = Garagem(**garagem.model_dump())
    db.add(db_garagem)
    db.commit()
    db.refresh(db_garagem)
    return db_garagem


def get_garagens(db: Session, skip: int = 0, limit: int = 100):
    """
    Returns all elements from the database table garagens
    """
    return db.query(Garagem).order_by(Garagem.id.desc()).offset(skip).limit(limit).all()


def get_garagem(db: Session, garagem_id: int):
    """
    Returns a specific element from the database table garagens
    """
    return db.query(Garagem).filter(Garagem.id == garagem_id).first()


def update_garagem(db: Session, garagem_id: int, garagem: GaragemUpdate):
    """
    Updates a specific element from the database table garagens
    """
    db_garagem = db.query(Garagem).filter(Garagem.id == garagem_id).first()

    if db_garagem is None:
        return None
    
    if garagem.apto_origem_id is not None:
        db_garagem.apto_origem_id = garagem.apto_origem_id
    if garagem.apto_destino_id is not None:
        db_garagem.apto_destino_id = garagem.apto_destino_id
    if garagem.checkin is not None:
        db_garagem.checkin = garagem.checkin
    if garagem.checkout is not None:
        db_garagem.checkout = garagem.checkout
    if garagem.diarias is not None:
        db_garagem.diarias = garagem.diarias
    if garagem.valor_diaria is not None:
        db_garagem.valor_diaria = garagem.valor_diaria
    if garagem.taxa_adm is not None:
        db_garagem.taxa_adm = garagem.taxa_adm
    if garagem.valor_total is not None:
        db_garagem.valor_total = garagem.valor_total
    if garagem.valor_imob is not None:
        db_garagem.valor_imob = garagem.valor_imob
    if garagem.valor_prop is not None:
        db_garagem.valor_prop = garagem.valor_prop
    
    db.commit()
    db.refresh(db_garagem)
    return db_garagem


def delete_garagem(db: Session, garagem_id: int):
    """
    Deletes a specific element from the database table garagens
    """
    db_garagem = db.query(Garagem).filter(Garagem.id == garagem_id).first()
    db.delete(db_garagem)
    db.commit()
    return db_garagem


def create_gasto(db: Session, gasto: GastoCreate):
    """
    Creates a new element in the database table gastos
    """
    db_gasto = Gasto(**gasto.model_dump())
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto


def get_gastos(db: Session, skip: int = 0, limit: int = 100):
    """
    Returns all elements from the database table gastos
    """
    return db.query(Gasto).order_by(Gasto.id.desc()).offset(skip).limit(limit).all()


def get_gasto(db: Session, gasto_id: int):
    """
    Returns a specific element from the database table gastos
    """
    return db.query(Gasto).filter(Gasto.id == gasto_id).first()


def update_gasto(db: Session, gasto_id: int, gasto: GastoUpdate):
    """
    Updates a specific element from the database table gastos
    """
    db_gasto = db.query(Gasto).filter(Gasto.id == gasto_id).first()

    if db_gasto is None:
        return None
    
    if gasto.apartamento_id is not None:
        db_gasto.apartamento_id = gasto.apartamento_id
    if gasto.data_pagamento is not None:
        db_gasto.data_pagamento = gasto.data_pagamento
    if gasto.valor_material is not None:
        db_gasto.valor_material = gasto.valor_material
    if gasto.valor_mo is not None:
        db_gasto.valor_mo = gasto.valor_mo
    if gasto.valor_total is not None:
        db_gasto.valor_total = gasto.valor_total
    if gasto.descricao is not None:
        db_gasto.descricao = gasto.descricao
    
    db.commit()
    db.refresh(db_gasto)
    return db_gasto


def delete_gasto(db: Session, gasto_id: int):
    """
    Deletes a specific element from the database table gastos
    """
    db_gasto = db.query(Gasto).filter(Gasto.id == gasto_id).first()
    db.delete(db_gasto)
    db.commit()
    return db_gasto


def create_proprietario(db: Session, proprietario: ProprietarioCreate):
    """
    Creates a new element in the database table proprietarios
    """
    db_proprietario = Proprietario(**proprietario.model_dump())
    db.add(db_proprietario)
    db.commit()
    db.refresh(db_proprietario)
    return db_proprietario


def get_proprietarios(db: Session, skip: int = 0, limit: int = 100):
    """
    Returns all elements from the database table proprietarios
    """
    return db.query(Proprietario).offset(skip).limit(limit).all()


def get_proprietario(db: Session, proprietario_id: int):
    """
    Returns a specific element from the database table proprietarios
    """
    return db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()


def update_proprietario(db: Session, proprietario_id: int, proprietario: ProprietarioUpdate):
    """
    Updates a specific element from the database table proprietarios
    """
    db_proprietario = db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()

    if db_proprietario is None:
        return None
    
    if proprietario.nome is not None:
        db_proprietario.nome = proprietario.nome
    if proprietario.cpf is not None:
        db_proprietario.cpf = proprietario.cpf
    if proprietario.telefone is not None:
        db_proprietario.telefone = proprietario.telefone
    if proprietario.email is not None:
        db_proprietario.email = proprietario.email
    
    db.commit()
    db.refresh(db_proprietario)
    return db_proprietario


def delete_proprietario(db: Session, proprietario_id: int):
    """
    Deletes a specific element from the database table proprietarios
    """
    db_proprietario = db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
    db.delete(db_proprietario)
    db.commit()
    return db_proprietario
