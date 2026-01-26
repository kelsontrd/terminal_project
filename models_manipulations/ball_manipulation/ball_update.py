from models.Ball import Ball
from db.db_base import get_session
import numpy as np


def ball_update(numbers):

    with get_session() as session:
        balls = session.query(Ball).all()
        array = np.array(numbers, dtype=int)
        for ball in balls:
            if ball.desc in array:
                # bola sorteada
                ball.frequency += 1
                ball.currente_sequence += 1
                ball.currente_delay = 0
                if ball.currente_sequence > ball.max_sequence:
                    ball.max_sequence = ball.currente_sequence
            else:
                # bola não sorteada
                ball.currente_delay += 1
                ball.currente_sequence = 0
                if ball.currente_delay > ball.max_delay:
                    ball.max_delay = ball.currente_delay

        try:
            session.commit()
        except Exception as e:
            print(f"Erro ao atualizar bolas: {e}")
            session.rollback()


# if __name__ == "__main__":
#     # exemplo de chamada
#     game_update([1, 5, 12, 24, 30])
