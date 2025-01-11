from sqlalchemy.orm import Session
from schemas import (
    AluguelCreate, AluguelUpdate,
    ApartamentoCreate, ApartamentoUpdate,
    DespesaCreate, DespesaUpdate,
    GaragemCreate, GaragemUpdate,
    EdificioCreate, EdificioUpdate,
    GastoCreate, GastoUpdate,
    ProprietarioCreate, ProprietarioUpdate,
    InquilinoCreate, InquilinoUpdate
)
from models import (
    Aluguel, Apartamento, Despesa, Edificio, Garagem, Gasto, Proprietario, Inquilino
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


def read_alugueis(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from the database table alugueis
    """
    return db.query(Aluguel).order_by(Aluguel.id.desc()).offset(offset).limit(limit).all()


def read_aluguel(db: Session, aluguel_id: int):
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


def read_apartamentos(db: Session, offset: int = 0, limit: int = 100):

    """
    Returns all elements from the database table apartamentos
    """
    return db.query(Apartamento).offset(offset).limit(limit).all()


def read_apartamento(db: Session, apartamento_id: int):
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


def read_despesas(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from the database table despesas
    """
    return db.query(Despesa).orderby(Despesa.id.desc()).offset(offset).limit(limit).all()


def read_despesa(db: Session, despesa_id: int):
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


def read_edificios(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from the database table edificios
    """
    return db.query(Edificio).offset(offset).limit(limit).all()


def read_edificio(db: Session, edificio_id: int):
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


def read_garagens(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from the database table garagens
    """
    return db.query(Garagem).order_by(Garagem.id.desc()).offset(offset).limit(limit).all()


def read_garagem(db: Session, garagem_id: int):
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


def read_gastos(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from the database table gastos
    """
    return db.query(Gasto).order_by(Gasto.id.desc()).offset(offset).limit(limit).all()


def read_gasto(db: Session, gasto_id: int):
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


def read_proprietarios(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from the database table proprietarios
    """
    return db.query(Proprietario).offset(offset).limit(limit).all()


def read_proprietario(db: Session, proprietario_id: int):
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


def create_inquilino(db: Session, inquilino: InquilinoCreate):
    """
    Creates a new element in the database table inquilinos
    """
    db_inquilino = Inquilino(**inquilino.model_dump())
    db.add(db_inquilino)
    db.commit()
    db.refresh(db_inquilino)
    return db_inquilino


def read_inquilinos(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from the database table inquilinos
    """
    return db.query(Inquilino).offset(offset).limit(limit).all()


def read_inquilino(db: Session, inquilino_id: int):
    """
    Returns a specific element from the database table inquilinos
    """
    return db.query(Inquilino).filter(Inquilino.id == inquilino_id).first()


def update_inquilino(db: Session, inquilino_id: int, inquilino: InquilinoUpdate):
    """
    Updates a specific element from the database table inquilinos
    """
    db_inquilino = db.query(Inquilino).filter(Inquilino.id == inquilino_id).first()

    if db_inquilino is None:
        return None
    
    if inquilino.apartamento is not None:
        db_inquilino.apartamento = inquilino.apartamento
    if inquilino.nome is not None:
        db_inquilino.nome = inquilino.nome
    if inquilino.tipo_residencia is not None:
        db_inquilino.tipo_residencia = inquilino.tipo_residencia
    if inquilino.cidade is not None:
        db_inquilino.cidade = inquilino.cidade
    if inquilino.cep is not None:
        db_inquilino.cep = inquilino.cep
    if inquilino.estado is not None:
        db_inquilino.estado = inquilino.estado
    if inquilino.pais is not None:
        db_inquilino.pais = inquilino.pais
    if inquilino.telefone is not None:
        db_inquilino.telefone = inquilino.telefone
    if inquilino.estado_civil is not None:
        db_inquilino.estado_civil = inquilino.estado_civil
    if inquilino.profissao is not None:
        db_inquilino.profissao = inquilino.profissao
    if inquilino.rg is not None:
        db_inquilino.rg = inquilino.rg
    if inquilino.cpf is not None:
        db_inquilino.cpf = inquilino.cpf
    if inquilino.mae is not None:
        db_inquilino.mae = inquilino.mae
    if inquilino.automovel is not None:
        db_inquilino.automovel = inquilino.automovel
    if inquilino.modelo_auto is not None:
        db_inquilino.modelo_auto = inquilino.modelo_auto
    if inquilino.placa_auto is not None:
        db_inquilino.placa_auto = inquilino.placa_auto
    if inquilino.cor_auto is not None:
        db_inquilino.cor_auto = inquilino.cor_auto
    if inquilino.checkin is not None:
        db_inquilino.checkin = inquilino.checkin
    if inquilino.checkout is not None:
        db_inquilino.checkout = inquilino.checkout
    if inquilino.observacoes is not None:
        db_inquilino.observacoes = inquilino.observacoes
    if inquilino.proprietario is not None:
        db_inquilino.proprietario = inquilino.proprietario
    if inquilino.imob_fone is not None:
        db_inquilino.imob_fone = inquilino.imob_fone
    if inquilino.acomp_01_nome is not None:
        db_inquilino.acomp_01_nome = inquilino.acomp_01_nome
    if inquilino.acomp_01_rg is not None:
        db_inquilino.acomp_01_rg = inquilino.acomp_01_rg
    if inquilino.acomp_01_cpf is not None:
        db_inquilino.acomp_01_cpf = inquilino.acomp_01_cpf
    if inquilino.acomp_01_idade is not None:
        db_inquilino.acomp_01_idade = inquilino.acomp_01_idade
    if inquilino.acomp_01_parentesco is not None:
        db_inquilino.acomp_01_parentesco = inquilino.acomp_01_parentesco
    if inquilino.acomp_02_nome is not None:
        db_inquilino.acomp_02_nome = inquilino.acomp_02_nome
    if inquilino.acomp_02_rg is not None:
        db_inquilino.acomp_02_rg = inquilino.acomp_02_rg
    if inquilino.acomp_02_cpf is not None:
        db_inquilino.acomp_02_cpf = inquilino.acomp_02_cpf
    if inquilino.acomp_02_idade is not None:
        db_inquilino.acomp_02_idade = inquilino.acomp_02_idade
    if inquilino.acomp_02_parentesco is not None:
        db_inquilino.acomp_02_parentesco = inquilino.acomp_02_parentesco
    if inquilino.acomp_03_nome is not None:
        db_inquilino.acomp_03_nome = inquilino.acomp_03_nome
    if inquilino.acomp_03_rg is not None:
        db_inquilino.acomp_03_rg = inquilino.acomp_03_rg
    if inquilino.acomp_03_cpf is not None:
        db_inquilino.acomp_03_cpf = inquilino.acomp_03_cpf
    if inquilino.acomp_03_idade is not None:
        db_inquilino.acomp_03_idade = inquilino.acomp_03_idade
    if inquilino.acomp_03_parentesco is not None:
        db_inquilino.acomp_03_parentesco = inquilino.acomp_03_parentesco
    if inquilino.acomp_04_nome is not None:
        db_inquilino.acomp_04_nome = inquilino.acomp_04_nome
    if inquilino.acomp_04_rg is not None:
        db_inquilino.acomp_04_rg = inquilino.acomp_04_rg
    if inquilino.acomp_04_cpf is not None:
        db_inquilino.acomp_04_cpf = inquilino.acomp_04_cpf
    if inquilino.acomp_04_idade is not None:
        db_inquilino.acomp_04_idade = inquilino.acomp_04_idade
    if inquilino.acomp_04_parentesco is not None:
        db_inquilino.acomp_04_parentesco = inquilino.acomp_04_parentesco
    if inquilino.acomp_05_nome is not None:
        db_inquilino.acomp_05_nome = inquilino.acomp_05_nome
    if inquilino.acomp_05_rg is not None:
        db_inquilino.acomp_05_rg = inquilino.acomp_05_rg
    if inquilino.acomp_05_cpf is not None:
        db_inquilino.acomp_05_cpf = inquilino.acomp_05_cpf
    if inquilino.acomp_05_idade is not None:
        db_inquilino.acomp_05_idade = inquilino.acomp_05_idade
    if inquilino.acomp_05_parentesco is not None:
        db_inquilino.acomp_05_parentesco = inquilino.acomp_05_parentesco
    if inquilino.acomp_06_nome is not None:
        db_inquilino.acomp_06_nome = inquilino.acomp_06_nome
    if inquilino.acomp_06_rg is not None:
        db_inquilino.acomp_06_rg = inquilino.acomp_06_rg
    if inquilino.acomp_06_cpf is not None:
        db_inquilino.acomp_06_cpf = inquilino.acomp_06_cpf
    if inquilino.acomp_06_idade is not None:
        db_inquilino.acomp_06_idade = inquilino.acomp_06_idade
    if inquilino.acomp_06_parentesco is not None:
        db_inquilino.acomp_06_parentesco = inquilino.acomp_06_parentesco
    if inquilino.acomp_07_nome is not None:
        db_inquilino.acomp_07_nome = inquilino.acomp_07_nome
    if inquilino.acomp_07_rg is not None:
        db_inquilino.acomp_07_rg = inquilino.acomp_07_rg
    if inquilino.acomp_07_cpf is not None:
        db_inquilino.acomp_07_cpf = inquilino.acomp_07_cpf
    if inquilino.acomp_07_idade is not None:
        db_inquilino.acomp_07_idade = inquilino.acomp_07_idade
    if inquilino.acomp_07_parentesco is not None:
        db_inquilino.acomp_07_parentesco = inquilino.acomp_07_parentesco
    if inquilino.acomp_08_nome is not None:
        db_inquilino.acomp_08_nome = inquilino.acomp_08_nome
    if inquilino.acomp_08_rg is not None:
        db_inquilino.acomp_08_rg = inquilino.acomp_08_rg
    if inquilino.acomp_08_cpf is not None:
        db_inquilino.acomp_08_cpf = inquilino.acomp_08_cpf
    if inquilino.acomp_08_idade is not None:
        db_inquilino.acomp_08_idade = inquilino.acomp_08_idade
    if inquilino.acomp_08_parentesco is not None:
        db_inquilino.acomp_08_parentesco = inquilino.acomp_08_parentesco
    if inquilino.acomp_09_nome is not None:
        db_inquilino.acomp_09_nome = inquilino.acomp_09_nome
    if inquilino.acomp_09_rg is not None:
        db_inquilino.acomp_09_rg = inquilino.acomp_09_rg
    if inquilino.acomp_09_cpf is not None:
        db_inquilino.acomp_09_cpf = inquilino.acomp_09_cpf
    if inquilino.acomp_09_idade is not None:
        db_inquilino.acomp_09_idade = inquilino.acomp_09_idade
    if inquilino.acomp_09_parentesco is not None:
        db_inquilino.acomp_09_parentesco = inquilino.acomp_09_parentesco
    if inquilino.acomp_10_nome is not None:
        db_inquilino.acomp_10_nome = inquilino.acomp_10_nome
    if inquilino.acomp_10_rg is not None:
        db_inquilino.acomp_10_rg = inquilino.acomp_10_rg
    if inquilino.acomp_10_cpf is not None:
        db_inquilino.acomp_10_cpf = inquilino.acomp_10_cpf
    if inquilino.acomp_10_idade is not None:
        db_inquilino.acomp_10_idade = inquilino.acomp_10_idade
    if inquilino.acomp_10_parentesco is not None:
        db_inquilino.acomp_10_parentesco = inquilino.acomp_10_parentesco

    db.commit()
    db.refresh(db_inquilino)
    return db_inquilino


def delete_inquilino(db: Session, inquilino_id: int):
    """
    Deletes a specific element from the database table inquilinos
    """
    db_inquilino = db.query(Inquilino).filter(Inquilino.id == inquilino_id).first()
    db.delete(db_inquilino)
    db.commit()
    return db_inquilino