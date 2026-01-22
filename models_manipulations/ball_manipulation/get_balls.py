from models.Ball import Ball
from models.Game import Game
from db.db_base import session


def get_balls(ball_number=None):
    try:
        if ball_number is None:
            balls = session.query(Ball).all()
        else:
            balls = session.query(Ball).filter(Ball.desc == ball_number).all()

        return balls
    except Exception as e:
        print(f"Erro ao buscar bolas: {e}")
        return None
