from db.db_base import session
from models_manipulations.game_manipulation.games_update.get_game_api import get_game
from sqlalchemy.orm import joinedload
from models.Game import Game
from models.Ball import Ball
import datetime
from models_manipulations.game_manipulation.GameCalcdata import GameCalcData
from models_manipulations.ball_manipulation.ball_update import ball_update

def game_update():
    # tras relações completas
    object_last_game_in_base = (session.query(Game).options(joinedload(Game.drawn_balls)).order_by(Game.id.desc()).first())
    last_game_in_base = [ball.desc for ball in object_last_game_in_base.drawn_balls]
    last_game_in_api = get_game()
    balls_map = {b.desc: b for b in session.query(Ball).all()} # aqui retorna todos os relacionamentos many to many com todos os seus campos em forma de dicionario
    #balls_map = {b.desc: b for b in session.query(Ball.desc).all()} # aqui retorna todos os relacionamentos many to many com apenas o campo desc em forma de dicionario
    if last_game_in_base is None:
        return {"error": "Nenhum jogo encontrado, tente reiniciar a base de dados!"}
    
    if last_game_in_base != last_game_in_api:
        print("Tabela de jogos desatualizada, iniciando atualização...")
        if last_game_in_api["numero"] - object_last_game_in_base.number == 1:
            ball_update(last_game_in_api["listaDezenas"])
            game_temp = Game(
                number = last_game_in_api["numero"],
                date = datetime.datetime.strptime(last_game_in_api["dataApuracao"], "%d/%m/%Y"),
                pairs=int(GameCalcData.cont_pairs(last_game_in_api["listaDezenas"])),
                sum_pairs=int(GameCalcData.sum_pairs(last_game_in_api["listaDezenas"])),
                odds=int(GameCalcData.cont_odds(last_game_in_api["listaDezenas"])),
                sum_odds=int(GameCalcData.sum_odds(last_game_in_api["listaDezenas"])),
                primes=int(GameCalcData.cont_primes(last_game_in_api["listaDezenas"])),
                sum_primes=int(GameCalcData.sum_primes(last_game_in_api["listaDezenas"])),
                fibonaccis=int(GameCalcData.cont_fibonaccis(last_game_in_api["listaDezenas"])),
                sum_fibonaccis=int(GameCalcData.sum_fibonaccis(last_game_in_api["listaDezenas"])),
                sum_general=int(GameCalcData.sum_array(last_game_in_api["listaDezenas"])),
                center=int(GameCalcData.cont_center(last_game_in_api["listaDezenas"])),
                sum_center=int(GameCalcData.sum_center(last_game_in_api["listaDezenas"])),
                border=int(GameCalcData.cont_border(last_game_in_api["listaDezenas"])),
                sum_border=int(GameCalcData.sum_border(last_game_in_api["listaDezenas"])), 
                repeated_previous_game=int(GameCalcData.count_repeated_previous_game(last_game_in_api["listaDezenas"], last_game_in_base)),
                pairs_repeated_previous_game=int(GameCalcData.count_pairs_repeated_previous_game(last_game_in_api["listaDezenas"], last_game_in_base)),
                odds_repeated_previous_game=int(GameCalcData.count_odds_repeated_previous_game(last_game_in_api["listaDezenas"], last_game_in_base)),
                primes_repeated_previous_game=int(GameCalcData.count_primes_repeated_previous_game(last_game_in_api["listaDezenas"], last_game_in_base)),
                fibonaccis_repeated_previous_game=int(GameCalcData.count_fibonaccis_repeated_previous_game(last_game_in_api["listaDezenas"], last_game_in_base)),
                center_repeated_previous_game=int(GameCalcData.cont_center_repeated_previous_game(last_game_in_api["listaDezenas"], last_game_in_base)),
                border_repeated_previous_game=int(GameCalcData.cont_border_repeated_previous_game(last_game_in_api["listaDezenas"], last_game_in_base)),  
                winners_15_hits=last_game_in_api["listaRateioPremio"][0]["numeroDeGanhadores"],
                winners_14_hits=last_game_in_api["listaRateioPremio"][1]["numeroDeGanhadores"],
                winners_13_hits=last_game_in_api["listaRateioPremio"][2]["numeroDeGanhadores"],
                winners_12_hits=last_game_in_api["listaRateioPremio"][3]["numeroDeGanhadores"],
                winners_11_hits=last_game_in_api["listaRateioPremio"][4]["numeroDeGanhadores"],
            )
            session.add(game_temp)
            with session.no_autoflush: 
                for ball_number in last_game_in_api["listaDezenas"]: 
                    ball_instance = balls_map.get(ball_number) 
                    if ball_instance: 
                        game_temp.drawn_balls.append(ball_instance)
            
            try:
                print(f"Inserindo jogo {game_temp.number} na base de dados...")
                # session.execute(delete(Game))  # Clear existing data
                session.add(game_temp)
                session.commit()
                print("Jogo inserido com sucesso.")
            except Exception as e:
                print(f"Erro ao inserir jogo: {e}")
                session.rollback()
        elif last_game_in_api["numero"] - object_last_game_in_base.number > 1:
            print(f"Atualizando jogos a partir de {object_last_game_in_base.number} até {last_game_in_api['numero']}...")
            update_games = []
            previous_game_balls = last_game_in_base
            
            for i in range(object_last_game_in_base.number + 1, last_game_in_api["numero"] + 1):
                last_game_in_api = get_game(i)
                ball_update(last_game_in_api["listaDezenas"])
                game_temp=Game(
                    number=last_game_in_api["numero"],
                    date=datetime.datetime.strptime(last_game_in_api["dataApuracao"], "%d/%m/%Y"),
                    pairs=int(GameCalcData.cont_pairs(last_game_in_api["listaDezenas"])),
                    sum_pairs=int(GameCalcData.sum_pairs(last_game_in_api["listaDezenas"])),
                    odds=int(GameCalcData.cont_odds(last_game_in_api["listaDezenas"])),
                    sum_odds=int(GameCalcData.sum_odds(last_game_in_api["listaDezenas"])),
                    primes=int(GameCalcData.cont_primes(last_game_in_api["listaDezenas"])),
                    sum_primes=int(GameCalcData.sum_primes(last_game_in_api["listaDezenas"])),
                    fibonaccis=int(GameCalcData.cont_fibonaccis(last_game_in_api["listaDezenas"])),
                    sum_fibonaccis=int(GameCalcData.sum_fibonaccis(last_game_in_api["listaDezenas"])),
                    sum_general=int(GameCalcData.sum_array(last_game_in_api["listaDezenas"])),
                    center=int(GameCalcData.cont_center(last_game_in_api["listaDezenas"])),
                    sum_center=int(GameCalcData.sum_center(last_game_in_api["listaDezenas"])),
                    border=int(GameCalcData.cont_border(last_game_in_api["listaDezenas"])),
                    sum_border=int(GameCalcData.sum_border(last_game_in_api["listaDezenas"])), 
                    repeated_previous_game=int(GameCalcData.count_repeated_previous_game(last_game_in_api["listaDezenas"], previous_game_balls)),
                    pairs_repeated_previous_game=int(GameCalcData.count_pairs_repeated_previous_game(last_game_in_api["listaDezenas"], previous_game_balls)),
                    odds_repeated_previous_game=int(GameCalcData.count_odds_repeated_previous_game(last_game_in_api["listaDezenas"], previous_game_balls)),
                    primes_repeated_previous_game=int(GameCalcData.count_primes_repeated_previous_game(last_game_in_api["listaDezenas"], previous_game_balls)),
                    fibonaccis_repeated_previous_game=int(GameCalcData.count_fibonaccis_repeated_previous_game(last_game_in_api["listaDezenas"], previous_game_balls)),
                    center_repeated_previous_game=int(GameCalcData.cont_center_repeated_previous_game(last_game_in_api["listaDezenas"], previous_game_balls)),
                    border_repeated_previous_game=int(GameCalcData.cont_border_repeated_previous_game(last_game_in_api["listaDezenas"], previous_game_balls)),  
                    winners_15_hits=last_game_in_api["listaRateioPremio"][0]["numeroDeGanhadores"],
                    winners_14_hits=last_game_in_api["listaRateioPremio"][1]["numeroDeGanhadores"],
                    winners_13_hits=last_game_in_api["listaRateioPremio"][2]["numeroDeGanhadores"],
                    winners_12_hits=last_game_in_api["listaRateioPremio"][3]["numeroDeGanhadores"],
                    winners_11_hits=last_game_in_api["listaRateioPremio"][4]["numeroDeGanhadores"],
                )
                session.add(game_temp)
                with session.no_autoflush: 
                    for ball_number in last_game_in_api["listaDezenas"]: 
                        ball_instance = balls_map.get(ball_number) 
                        if ball_instance: 
                            game_temp.drawn_balls.append(ball_instance)
                update_games.append(game_temp)
                previous_game_balls = last_game_in_api["listaDezenas"]
            try:
                print("Inserindo jogos na base de dados...")
                session.add_all(update_games)
                session.commit()
                print("Games inseridos com sucesso.")
            except Exception as e:
                print(f"Erro ao inserir jogos: {e}")
                session.rollback()
        else:
            print(f"Base de dados já está atualizada.")
if __name__ == "__main__":
    game_update()