from db.db_base import Base,engine
from models.Tarefa import Tarefa
from models.Ball import Ball

# Cria tabelas 
def db_create_tables():
    # Cria todas as tabelas definidas no modelo
    Base.metadata.create_all(engine)
