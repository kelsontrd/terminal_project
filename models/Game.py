from sqlalchemy import Column, Integer, ManyToMany
from db.db_base import Base
from models.Timestump import Timestump
from models.Ball import Ball

# Modelo da tabela de bolas
class Game(Timestump, Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)
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
    drawn_balls = ManyToMany(Ball, secondary="game_ball")
    