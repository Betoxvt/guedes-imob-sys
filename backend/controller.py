from database import Base, engine, SessionLocal
from models import Aluguel, Apartamento, DespesaFixa, Garagem, GastoVariavel, Proprietario
from schemas import AluguelSchema, ApartamentoSchema, DespesaFixaSchema, GaragemSchema, GastoVariavelSchema, ProprietarioSchema

# Criar as tabelas no banco
def create_tables():
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")
