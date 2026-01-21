from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from db.db_base import Base
from models.Timestump import Timestump

# Modelo da tabela de bolas
class Ball(Timestump, Base):
    __tablename__ = "balls"
    id = Column(Integer, primary_key=True)
    desc = Column(Integer, unique=True)
    frequency = Column(Integer)
    currente_sequence = Column(Integer)
    max_sequence = Column(Integer)
    currente_delay = Column(Integer)
    max_delay = Column(Integer)

    #Relação Many-to-Many com Game    
    games = relationship(
        "Game",
        secondary="game_ball",
        back_populates="drawn_balls",
    )