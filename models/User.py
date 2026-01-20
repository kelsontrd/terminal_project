from sqlalchemy import Column, Integer, String
from db.db_base import Base
from models.Timestump import Timestump

# Modelo da tabela de usuários
class User(Timestump, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    key = Column(String(8), unique=True)
   
    