from util.json_manipulation import load_json
from models_manipulations.game_manipulation.GameCalcdata import GameCalcData
from sqlalchemy import delete
from models.Game import Game, game_ball
from models.Ball import Ball
from db.db_base import session
import datetime

# Inicia a base de dados de jogos, carrega os dados do JSON e insere na tabela Game
# Usada para apagar todo o banco de dados e inserir os dados novamente

def game_init_base():
    session.execute(delete(Game))
    session.execute(delete(game_ball))
    session.commit()
    data_games = load_json("base_games")
    games = []
    previous_game_balls = None
    # Pré-carrega todas as bolas em memória para evitar milhares de queries 
    balls_map = {b.desc: b for b in session.query(Ball).all()}
    print("Criando instâncias de jogos Aguarde...")
    for game in data_games:
        game_temp = Game(
                number=game["concurso"],
                date=datetime.datetime.strptime(game["data"], "%d/%m/%Y"),
                pairs=int(GameCalcData.cont_pairs(game["drawn_numbers"])),
                sum_pairs=int(GameCalcData.sum_pairs(game["drawn_numbers"])),
                odds=int(GameCalcData.cont_odds(game["drawn_numbers"])),
                sum_odds=int(GameCalcData.sum_odds(game["drawn_numbers"])),
                primes=int(GameCalcData.cont_primes(game["drawn_numbers"])),
                sum_primes=int(GameCalcData.sum_primes(game["drawn_numbers"])),
                fibonaccis=int(GameCalcData.cont_fibonaccis(game["drawn_numbers"])),
                sum_fibonaccis=int(GameCalcData.sum_fibonaccis(game["drawn_numbers"])),
                sum_general=int(GameCalcData.sum_array(game["drawn_numbers"])),
                center=int(GameCalcData.cont_center(game["drawn_numbers"])),
                sum_center=int(GameCalcData.sum_center(game["drawn_numbers"])),
                border=int(GameCalcData.cont_border(game["drawn_numbers"])),
                sum_border=int(GameCalcData.sum_border(game["drawn_numbers"])), 
                repeated_previous_game=int(GameCalcData.count_repeated_previous_game(game["drawn_numbers"], previous_game_balls)),
                pairs_repeated_previous_game=int(GameCalcData.count_pairs_repeated_previous_game(game["drawn_numbers"], previous_game_balls)),
                odds_repeated_previous_game=int(GameCalcData.count_odds_repeated_previous_game(game["drawn_numbers"], previous_game_balls)),
                primes_repeated_previous_game=int(GameCalcData.count_primes_repeated_previous_game(game["drawn_numbers"], previous_game_balls)),
                fibonaccis_repeated_previous_game=int(GameCalcData.count_fibonaccis_repeated_previous_game(game["drawn_numbers"], previous_game_balls)),
                center_repeated_previous_game=int(GameCalcData.cont_center_repeated_previous_game(game["drawn_numbers"], previous_game_balls)),
                border_repeated_previous_game=int(GameCalcData.cont_border_repeated_previous_game(game["drawn_numbers"], previous_game_balls)),
                winners_15_hits=game["winners_15_hits"],
                winners_14_hits=game["winners_14_hits"],
                winners_13_hits=game["winners_13_hits"],
                winners_12_hits=game["winners_12_hits"],
                winners_11_hits=game["winners_11_hits"],
            )
        session.add(game_temp)
        with session.no_autoflush: 
            for ball_number in game["drawn_numbers"]: 
                ball_instance = balls_map.get(ball_number) 
                if ball_instance: 
                    game_temp.drawn_balls.append(ball_instance)
        games.append(game_temp)
        previous_game_balls = game["drawn_numbers"]
    try:
        print("Inserindo jogos na base de dados...")
        # session.execute(delete(Game))  # Clear existing data
        session.add_all(games)
        session.commit()
        print("Games inseridos com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir jogos: {e}")
        session.rollback()
if __name__ == "__main__":
    print("Executando game_init_base.py diretamente...")
    game_init_base()