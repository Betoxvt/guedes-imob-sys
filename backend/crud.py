from sqlalchemy.orm import Session
from schemas import (
    AluguelBase, AluguelCreate, AluguelUpdate,
    ApartamentoBase, ApartamentoCreate, ApartamentoUpdate,
    DespesaBase, DespesaCreate, DespesaUpdate,
    GaragemBase,GaragemCreate, GaragemUpdate,
    EdificioBase, EdificioCreate, EdificioUpdate,
    GastoBase, GastoCreate, GastoUpdate,
    ProprietarioBase, ProprietarioCreate, ProprietarioUpdate
)
from models import (
    Aluguel, Apartamento, Despesa, Edificio, Garagem, Gasto, Proprietario
)


def get_alugueis(db: Session):
    """
    Returns all elements from the database table alugueis
    """
    return db.query(Aluguel).all()

def get_aluguel(db: Session, aluguel_id: int):
    """
    Returns a specific element from the database table alugueis
    """
    return db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()