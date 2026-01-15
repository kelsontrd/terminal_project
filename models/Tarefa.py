from sqlalchemy import Column, Integer, String, create_engine
from db.db_base import Base

# Modelo da tabela de tarefas
class Tarefa(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    