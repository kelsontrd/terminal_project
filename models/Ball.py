from sqlalchemy import Column, Integer
from db.db_base import Base
from models.Timestump import Timestump

# Modelo da tabela de bolas
class Ball(Timestump, Base):
    __tablename__ = "balls"
    id = Column(Integer, primary_key=True)
    desc = Column(Integer, unique=True)
    frequency = Column(Integer)
    max_sequence = Column(Integer)
    currente_delay = Column(Integer)
    max_delay = Column(Integer)
    