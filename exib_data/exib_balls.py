from models_manipulations.ball_manipulation.get_balls import get_balls
from models.Ball import Ball

def exib_balls(Ball = None):
    balls = get_balls()
    if balls is None:
        balls = get_balls()
    else:
        balls = get_balls(Ball)
    
    for ball in balls:
        print(f"Bola: {ball.desc} | Frequência: {ball.frequency} | Sequência Atual: {ball.currente_sequence} | Sequência Máxima: {ball.max_sequence} | Delay Atual: {ball.currente_delay} | Delay Máximo: {ball.max_delay}")