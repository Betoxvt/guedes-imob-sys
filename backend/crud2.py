from models import Aluguel, Apartamento, Despesa, Garagem, Proprietario, Ficha
from sqlalchemy.orm import Session
from schemas2 import (
    AluguelCreate, AluguelUpdate,
    ApartamentoCreate, ApartamentoUpdate,
    DespesaCreate, DespesaUpdate,
    GaragemCreate, GaragemUpdate,
    ProprietarioCreate, ProprietarioUpdate,
    FichaCreate, FichaUpdate
)


def create_aluguel(db: Session, aluguel: AluguelCreate) -> Aluguel:
    """
    Creates a new element in database table alugueis
    """
    try:
        db_aluguel = Aluguel(**aluguel.model_dump())
        db.add(db_aluguel)
        db.commit()
        db.refresh(db_aluguel)
        return db_aluguel
    except Exception as e:
        print(f'Erro ao registrar aluguel: {e}')
        db.rollback()
        raise e


def read_alugueis(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table alugueis
    """
    try:
        return db.query(Aluguel).order_by(Aluguel.id.desc()).offset(offset).limit(limit).all()
    except Exception as e:
        print(f'Erro ao buscar aluguéis: {e}')
        raise e


def read_aluguel(db: Session, aluguel_id: int):
    """
    Returns a specific element from database table alugueis
    """
    try:
        return db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
    except Exception as e:
        print(f'Erro ao buscar aluguel: {e}')
        raise e


def update_aluguel(db: Session, aluguel_id: int, aluguel: AluguelUpdate) -> bool:
    """
    Updates a specific element from database table alugueis
    """
    try:
        db_aluguel = db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
        if db_aluguel is None:
            return False
    
        db.query(Aluguel).filter(Aluguel.id == aluguel_id).update(aluguel.model_dump())
        db.commit()
        db.refresh(db_aluguel)
        return True
    except Exception as e:
        print(f'Erro ao atualizar aluguel: {e}')
        db.rollback()
        return False


def delete_aluguel(db: Session, aluguel_id: int):
    """
    Deletes a specific element from database table alugueis
    """
    try:
        db_aluguel = db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
        db.delete(db_aluguel)
        db.commit()
        return db_aluguel
    except Exception as e:
        print(f'Erro ao deletar aluguel: {e}')
        db.rollback()
        raise e


def create_apartamento(db: Session, apartamento: ApartamentoCreate) -> Apartamento:
    """
    Creates a new element in database table apartamentos
    """
    try:
        db_apartamento = Apartamento(**apartamento.model_dump())
        db.add(db_apartamento)
        db.commit()
        db.refresh(db_apartamento)
        return db_apartamento
    except Exception as e:
        print(f'Erro ao registrar apartamento: {e}')
        db.rollback()
        raise e


def read_apartamentos(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table apartamentos
    """
    try:
        return db.query(Apartamento).order_by(Apartamento.id.desc()).offset(offset).limit(limit).all()
    except Exception as e:
        print(f'Erro ao buscar apartamentos: {e}')
        raise e


def read_apartamento(db: Session, apartamento_id: int):
    """
    Returns a specific element from database table apartamentos
    """
    try:
        return db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
    except Exception as e:
        print(f'Erro ao buscar apartamento: {e}')
        raise e


def update_apartamento(db: Session, apartamento_id: int, apartamento: ApartamentoUpdate) -> bool:
    """
    Updates a specific element from database table apartamentos
    """
    try:
        db_apartamento = db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
        if db_apartamento is None:
            return False
    
        db.query(Apartamento).filter(Apartamento.id == apartamento_id).update(apartamento.model_dump())
        db.commit()
        db.refresh(db_apartamento)
        return True
    except Exception as e:
        print(f'Erro ao atualizar apartamento: {e}')
        db.rollback()
        return False


def delete_apartamento(db: Session, apartamento_id: int):
    """
    Deletes a specific element from database table apartamentos
    """
    try:
        db_apartamento = db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
        db.delete(db_apartamento)
        db.commit()
        return db_apartamento
    except Exception as e:
        print(f'Erro ao deletar apartamento: {e}')
        db.rollback()
        raise e


def create_despesa(db: Session, despesa: DespesaCreate) -> Despesa:
    """
    Creates a new element in database table despesas
    """
    try:
        db_despesa = Despesa(**despesa.model_dump())
        db.add(db_despesa)
        db.commit()
        db.refresh(db_despesa)
        return db_despesa
    except Exception as e:
        print(f'Erro ao registrar despesa: {e}')
        db.rollback()
        raise e


def read_despesas(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table despesas
    """
    try:
        return db.query(Despesa).order_by(Despesa.id.desc()).offset(offset).limit(limit).all()
    except Exception as e:
        print(f'Erro ao buscar despesas: {e}')
        raise e


def read_despesa(db: Session, despesa_id: int):
    """
    Returns a specific element from database table despesas
    """
    try:
        return db.query(Despesa).filter(Despesa.id == despesa_id).first()
    except Exception as e:
        print(f'Erro ao buscar despesa: {e}')
        raise e


def update_despesa(db: Session, despesa_id: int, despesa: DespesaUpdate) -> bool:
    """
    Updates a specific element from database table despesas
    """
    try:
        db_despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
        if db_despesa is None:
            return False
    
        db.query(Despesa).filter(Despesa.id == despesa_id).update(despesa.model_dump())
        db.commit()
        db.refresh(db_despesa)
        return True
    except Exception as e:
        print(f'Erro ao atualizar despesa: {e}')
        db.rollback()
        return False


def delete_despesa(db: Session, despesa_id: int):
    """
    Deletes a specific element from database table despesas
    """
    try:
        db_despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
        db.delete(db_despesa)
        db.commit()
        return db_despesa
    except Exception as e:
        print(f'Erro ao deletar despesa: {e}')
        db.rollback()
        raise e


def create_garagem(db: Session, garagem: GaragemCreate) -> Garagem:
    """
    Creates a new element in database table garagens
    """
    try:
        db_garagem = Garagem(**garagem.model_dump())
        db.add(db_garagem)
        db.commit()
        db.refresh(db_garagem)
        return db_garagem
    except Exception as e:
        print(f'Erro ao registrar garagem: {e}')
        db.rollback()
        raise e


def read_garagens(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table garagens
    """
    try:
        return db.query(Garagem).order_by(Garagem.id.desc()).offset(offset).limit(limit).all()
    except Exception as e:
        print(f'Erro ao buscar garagens: {e}')
        raise e


def read_garagem(db: Session, garagem_id: int):
    """
    Returns a specific element from database table garagens
    """
    try:
        return db.query(Garagem).filter(Garagem.id == garagem_id).first()
    except Exception as e:
        print(f'Erro ao buscar garagem: {e}')
        raise e


def update_garagem(db: Session, garagem_id: int, garagem: GaragemUpdate) -> bool:
    """
    Updates a specific element from database table garagens
    """
    try:
        db_garagem = db.query(Garagem).filter(Garagem.id == garagem_id).first()
        if db_garagem is None:
            return False
    
        db.query(Garagem).filter(Garagem.id == garagem_id).update(garagem.model_dump())
        db.commit()
        db.refresh(db_garagem)
        return True
    except Exception as e:
        print(f'Erro ao atualizar garagem: {e}')
        db.rollback()
        return False


def delete_garagem(db: Session, garagem_id: int):
    """
    Deletes a specific element from database table garagens
    """
    try:
        db_garagem = db.query(Garagem).filter(Garagem.id == garagem_id).first()
        db.delete(db_garagem)
        db.commit()
        return db_garagem
    except Exception as e:
        print(f'Erro ao deletar garagem: {e}')
        db.rollback()
        raise e


def create_proprietario(db: Session, proprietario: ProprietarioCreate) -> Proprietario:
    """
    Creates a new element in database table proprietarios
    """
    try:
        db_proprietario = Proprietario(**proprietario.model_dump())
        db.add(db_proprietario)
        db.commit()
        db.refresh(db_proprietario)
        return db_proprietario
    except Exception as e:
        print(f'Erro ao registrar proprietario: {e}')
        db.rollback()
        raise e


def read_proprietarios(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table proprietarios
    """
    try:
        return db.query(Proprietario).order_by(Proprietario.id.desc()).offset(offset).limit(limit).all()
    except Exception as e:
        print(f'Erro ao buscar proprietarios: {e}')
        raise e


def read_proprietario(db: Session, proprietario_id: int):
    """
    Returns a specific element from database table proprietarios
    """
    try:
        return db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
    except Exception as e:
        print(f'Erro ao buscar proprietario: {e}')
        raise e


def update_proprietario(db: Session, proprietario_id: int, proprietario: ProprietarioUpdate) -> bool:
    """
    Updates a specific element from database table proprietarios
    """
    try:
        db_proprietario = db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
        if db_proprietario is None:
            return False
    
        db.query(Proprietario).filter(Proprietario.id == proprietario_id).update(proprietario.model_dump())
        db.commit()
        db.refresh(db_proprietario)
        return True
    except Exception as e:
        print(f'Erro ao atualizar proprietario: {e}')
        db.rollback()
        return False


def delete_proprietario(db: Session, proprietario_id: int):
    """
    Deletes a specific element from database table proprietario
    """
    try:
        db_proprietario = db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
        db.delete(db_proprietario)
        db.commit()
        return db_proprietario
    except Exception as e:
        print(f'Erro ao deletar proprietario: {e}')
        db.rollback()
        raise e


def create_ficha(db: Session, ficha: FichaCreate) -> Ficha:
    """
    Creates a new element in database table fichas
    """
    try:
        db_ficha = Ficha(**ficha.model_dump())
        db.add(db_ficha)
        db.commit()
        db.refresh(db_ficha)
        return db_ficha
    except Exception as e:
        print(f'Erro ao registrar ficha: {e}')
        db.rollback()
        raise e


def read_fichas(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table fichas
    """
    try:
        return db.query(Ficha).order_by(Ficha.id.desc()).offset(offset).limit(limit).all()
    except Exception as e:
        print(f'Erro ao buscar fichas: {e}')
        raise e


def read_ficha(db: Session, ficha_id: int):
    """
    Returns a specific element from database table fichas
    """
    try:
        return db.query(Ficha).filter(Ficha.id == ficha_id).first()
    except Exception as e:
        print(f'Erro ao buscar ficha: {e}')
        raise e


def update_ficha(db: Session, ficha_id: int, ficha: FichaUpdate) -> bool:
    """
    Updates a specific element from database table fichas
    
    """
    try:
        db_ficha = db.query(Ficha).filter(Ficha.id == ficha_id).first()
        if db_ficha is None:
            return False
    
        db.query(Ficha).filter(Ficha.id == ficha_id).update(ficha.model_dump())
        db.commit()
        db.refresh(db_ficha)
        return True
    except Exception as e:
        print(f'Erro ao atualizar ficha: {e}')
        db.rollback()
        return False


def delete_ficha(db: Session, ficha_id: int):
    """
    Deletes a specific element from database table fichas
    """
    try:
        db_ficha = db.query(Ficha).filter(Ficha.id == ficha_id).first()
        db.delete(db_ficha)
        db.commit()
        return db_ficha
    except Exception as e:
        print(f'Erro ao deletar ficha: {e}')
        db.rollback()
        raise e

