from sqlmodel import SQLModel, create_engine
from schemas import Aluguel, Apartamento, DespesaFixa, Garagem, GastoVariavel, Proprietario  

DATABASE_URL = "sqlite:///data/imob_db.sqlite"

# Crie o engine para o SQLite
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
    print("Banco de dados e tabelas criados com sucesso!")
    