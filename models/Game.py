from sqlalchemy import Column, Integer, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.Ball import Ball
from db.db_base import Base
from models.Timestump import Timestump

# Modelo da tabela de bolas
class Game(Timestump, Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)
    date = Column(DateTime)
    pairs = Column(Integer)
    sum_pairs = Column(Integer)
    odds = Column(Integer)
    sum_odds = Column(Integer)
    primes = Column(Integer)
    sum_primes = Column(Integer)
    fibonaccis = Column(Integer)
    sum_fibonaccis = Column(Integer)
    sum_general = Column(Integer)
    center = Column(Integer)
    sum_center = Column(Integer)
    border = Column(Integer)
    sum_border = Column(Integer)
    repeated_previous_game = Column(Integer)
    pairs_repeated_previous_game = Column(Integer)
    odds_repeated_previous_game = Column(Integer)
    primes_repeated_previous_game = Column(Integer)
    fibonaccis_repeated_previous_game = Column(Integer)
    center_repeated_previous_game = Column(Integer)
    border_repeated_previous_game = Column(Integer)
    winners_15_hits = Column(Integer)
    winners_14_hits = Column(Integer)
    winners_13_hits = Column(Integer)
    winners_12_hits = Column(Integer)
    winners_11_hits = Column(Integer)

    # Relação Many-to-Many com Ball
    drawn_balls = relationship(
        "Ball",
        secondary="game_ball",
        back_populates="games",
        #back_populates="games", # se usado não pre
    )

# Tabela de associação entre Game e Ball
game_ball = Table(
    "game_ball",
    Base.metadata,
    Column("games_id", Integer, ForeignKey("games.id"), primary_key=True),
    Column("balls_id", Integer, ForeignKey("balls.id"), primary_key=True),
)