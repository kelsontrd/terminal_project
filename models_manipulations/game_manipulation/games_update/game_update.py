# from db.db_base import get_session
# from models_manipulations.game_manipulation.games_update.get_game_api import get_game
# from sqlalchemy.orm import joinedload
# from models.Game import Game
# from models.Ball import Ball
# import datetime
# from models_manipulations.game_manipulation.GameCalcdata import GameCalcData
# from models_manipulations.ball_manipulation.ball_update import ball_update


# def game_update():
#     with get_session() as session:
#         # tras relações completas
#         object_last_game_in_base = (
#             session.query(Game)
#             .options(joinedload(Game.drawn_balls))
#             .order_by(Game.id.desc())
#             .first()
#         )
#         last_game_in_base = [ball.desc for ball in object_last_game_in_base.drawn_balls]
#         last_game_in_api = get_game()
#         balls_map = {
#             b.desc: b for b in session.query(Ball).all()
#         }  # aqui retorna todos os relacionamentos many to many com todos os seus campos em forma de dicionario
#         # balls_map = {b.desc: b for b in session.query(Ball.desc).all()} # aqui retorna todos os relacionamentos many to many com apenas o campo desc em forma de dicionario
#         if last_game_in_base is None:
#             return {"error": "Nenhum jogo encontrado, tente reiniciar a base de dados!"}

#         if last_game_in_base != last_game_in_api:
#             print("Tabela de jogos desatualizada, iniciando atualização...")
#             with get_session() as session:
#                 if last_game_in_api["numero"] - object_last_game_in_base.number == 1:
#                     ball_update(last_game_in_api["listaDezenas"])
#                     game_temp = Game(
#                         number=last_game_in_api["numero"],
#                         date=datetime.datetime.strptime(
#                             last_game_in_api["dataApuracao"], "%d/%m/%Y"
#                         ),
#                         pairs=int(
#                             GameCalcData.cont_pairs(last_game_in_api["listaDezenas"])
#                         ),
#                         sum_pairs=int(
#                             GameCalcData.sum_pairs(last_game_in_api["listaDezenas"])
#                         ),
#                         odds=int(
#                             GameCalcData.cont_odds(last_game_in_api["listaDezenas"])
#                         ),
#                         sum_odds=int(
#                             GameCalcData.sum_odds(last_game_in_api["listaDezenas"])
#                         ),
#                         primes=int(
#                             GameCalcData.cont_primes(last_game_in_api["listaDezenas"])
#                         ),
#                         sum_primes=int(
#                             GameCalcData.sum_primes(last_game_in_api["listaDezenas"])
#                         ),
#                         fibonaccis=int(
#                             GameCalcData.cont_fibonaccis(
#                                 last_game_in_api["listaDezenas"]
#                             )
#                         ),
#                         sum_fibonaccis=int(
#                             GameCalcData.sum_fibonaccis(
#                                 last_game_in_api["listaDezenas"]
#                             )
#                         ),
#                         sum_general=int(
#                             GameCalcData.sum_array(last_game_in_api["listaDezenas"])
#                         ),
#                         center=int(
#                             GameCalcData.cont_center(last_game_in_api["listaDezenas"])
#                         ),
#                         sum_center=int(
#                             GameCalcData.sum_center(last_game_in_api["listaDezenas"])
#                         ),
#                         border=int(
#                             GameCalcData.cont_border(last_game_in_api["listaDezenas"])
#                         ),
#                         sum_border=int(
#                             GameCalcData.sum_border(last_game_in_api["listaDezenas"])
#                         ),
#                         repeated_previous_game=int(
#                             GameCalcData.count_repeated_previous_game(
#                                 last_game_in_api["listaDezenas"], last_game_in_base
#                             )
#                         ),
#                         pairs_repeated_previous_game=int(
#                             GameCalcData.count_pairs_repeated_previous_game(
#                                 last_game_in_api["listaDezenas"], last_game_in_base
#                             )
#                         ),
#                         odds_repeated_previous_game=int(
#                             GameCalcData.count_odds_repeated_previous_game(
#                                 last_game_in_api["listaDezenas"], last_game_in_base
#                             )
#                         ),
#                         primes_repeated_previous_game=int(
#                             GameCalcData.count_primes_repeated_previous_game(
#                                 last_game_in_api["listaDezenas"], last_game_in_base
#                             )
#                         ),
#                         fibonaccis_repeated_previous_game=int(
#                             GameCalcData.count_fibonaccis_repeated_previous_game(
#                                 last_game_in_api["listaDezenas"], last_game_in_base
#                             )
#                         ),
#                         center_repeated_previous_game=int(
#                             GameCalcData.cont_center_repeated_previous_game(
#                                 last_game_in_api["listaDezenas"], last_game_in_base
#                             )
#                         ),
#                         border_repeated_previous_game=int(
#                             GameCalcData.cont_border_repeated_previous_game(
#                                 last_game_in_api["listaDezenas"], last_game_in_base
#                             )
#                         ),
#                         winners_15_hits=last_game_in_api["listaRateioPremio"][0][
#                             "numeroDeGanhadores"
#                         ],
#                         winners_14_hits=last_game_in_api["listaRateioPremio"][1][
#                             "numeroDeGanhadores"
#                         ],
#                         winners_13_hits=last_game_in_api["listaRateioPremio"][2][
#                             "numeroDeGanhadores"
#                         ],
#                         winners_12_hits=last_game_in_api["listaRateioPremio"][3][
#                             "numeroDeGanhadores"
#                         ],
#                         winners_11_hits=last_game_in_api["listaRateioPremio"][4][
#                             "numeroDeGanhadores"
#                         ],
#                     )
#                     session.add(game_temp)
#                     with session.no_autoflush:
#                         for ball_number in last_game_in_api["listaDezenas"]:
#                             ball_instance = balls_map.get(ball_number)
#                             if ball_instance:
#                                 game_temp.drawn_balls.append(ball_instance)

#                     try:
#                         print(f"Inserindo jogo {game_temp.number} na base de dados...")
#                         # session.execute(delete(Game))  # Clear existing data
#                         session.add(game_temp)
#                         session.commit()
#                         print("Jogo inserido com sucesso.")
#                     except Exception as e:
#                         print(f"Erro ao inserir jogo: {e}")
#                         session.rollback()
#                 elif last_game_in_api["numero"] - object_last_game_in_base.number > 1:
#                     print(
#                         f"Atualizando jogos a partir de {object_last_game_in_base.number} até {last_game_in_api['numero']}..."
#                     )
#                     update_games = []
#                     previous_game_balls = last_game_in_base

#                     for i in range(
#                         object_last_game_in_base.number + 1,
#                         last_game_in_api["numero"] + 1,
#                     ):
#                         last_game_in_api = get_game(i)
#                         ball_update(last_game_in_api["listaDezenas"])
#                         game_temp = Game(
#                             number=last_game_in_api["numero"],
#                             date=datetime.datetime.strptime(
#                                 last_game_in_api["dataApuracao"], "%d/%m/%Y"
#                             ),
#                             pairs=int(
#                                 GameCalcData.cont_pairs(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             sum_pairs=int(
#                                 GameCalcData.sum_pairs(last_game_in_api["listaDezenas"])
#                             ),
#                             odds=int(
#                                 GameCalcData.cont_odds(last_game_in_api["listaDezenas"])
#                             ),
#                             sum_odds=int(
#                                 GameCalcData.sum_odds(last_game_in_api["listaDezenas"])
#                             ),
#                             primes=int(
#                                 GameCalcData.cont_primes(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             sum_primes=int(
#                                 GameCalcData.sum_primes(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             fibonaccis=int(
#                                 GameCalcData.cont_fibonaccis(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             sum_fibonaccis=int(
#                                 GameCalcData.sum_fibonaccis(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             sum_general=int(
#                                 GameCalcData.sum_array(last_game_in_api["listaDezenas"])
#                             ),
#                             center=int(
#                                 GameCalcData.cont_center(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             sum_center=int(
#                                 GameCalcData.sum_center(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             border=int(
#                                 GameCalcData.cont_border(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             sum_border=int(
#                                 GameCalcData.sum_border(
#                                     last_game_in_api["listaDezenas"]
#                                 )
#                             ),
#                             repeated_previous_game=int(
#                                 GameCalcData.count_repeated_previous_game(
#                                     last_game_in_api["listaDezenas"],
#                                     previous_game_balls,
#                                 )
#                             ),
#                             pairs_repeated_previous_game=int(
#                                 GameCalcData.count_pairs_repeated_previous_game(
#                                     last_game_in_api["listaDezenas"],
#                                     previous_game_balls,
#                                 )
#                             ),
#                             odds_repeated_previous_game=int(
#                                 GameCalcData.count_odds_repeated_previous_game(
#                                     last_game_in_api["listaDezenas"],
#                                     previous_game_balls,
#                                 )
#                             ),
#                             primes_repeated_previous_game=int(
#                                 GameCalcData.count_primes_repeated_previous_game(
#                                     last_game_in_api["listaDezenas"],
#                                     previous_game_balls,
#                                 )
#                             ),
#                             fibonaccis_repeated_previous_game=int(
#                                 GameCalcData.count_fibonaccis_repeated_previous_game(
#                                     last_game_in_api["listaDezenas"],
#                                     previous_game_balls,
#                                 )
#                             ),
#                             center_repeated_previous_game=int(
#                                 GameCalcData.cont_center_repeated_previous_game(
#                                     last_game_in_api["listaDezenas"],
#                                     previous_game_balls,
#                                 )
#                             ),
#                             border_repeated_previous_game=int(
#                                 GameCalcData.cont_border_repeated_previous_game(
#                                     last_game_in_api["listaDezenas"],
#                                     previous_game_balls,
#                                 )
#                             ),
#                             winners_15_hits=last_game_in_api["listaRateioPremio"][0][
#                                 "numeroDeGanhadores"
#                             ],
#                             winners_14_hits=last_game_in_api["listaRateioPremio"][1][
#                                 "numeroDeGanhadores"
#                             ],
#                             winners_13_hits=last_game_in_api["listaRateioPremio"][2][
#                                 "numeroDeGanhadores"
#                             ],
#                             winners_12_hits=last_game_in_api["listaRateioPremio"][3][
#                                 "numeroDeGanhadores"
#                             ],
#                             winners_11_hits=last_game_in_api["listaRateioPremio"][4][
#                                 "numeroDeGanhadores"
#                             ],
#                         )
#                         session.add(game_temp)
#                         with session.no_autoflush:
#                             for ball_number in last_game_in_api["listaDezenas"]:
#                                 ball_instance = balls_map.get(ball_number)
#                                 if ball_instance:
#                                     game_temp.drawn_balls.append(ball_instance)
#                         update_games.append(game_temp)
#                         previous_game_balls = last_game_in_api["listaDezenas"]
#                     try:
#                         print("Inserindo jogos na base de dados...")
#                         session.add_all(update_games)
#                         session.commit()
#                         print("Games inseridos com sucesso.")
#                     except Exception as e:
#                         print(f"Erro ao inserir jogos: {e}")
#                         session.rollback()
#                 else:
#                     print(f"Base de dados já está atualizada.")


# if __name__ == "__main__":
#     game_update()

from db.db_base import get_session
from models_manipulations.game_manipulation.games_update.get_game_api import get_game
from sqlalchemy.orm import joinedload
from models.Game import Game
from models.Ball import Ball
import datetime
from models_manipulations.game_manipulation.GameCalcdata import GameCalcData
from models_manipulations.ball_manipulation.ball_update import ball_update


def create_game_object(api_game, previous_game, balls_map):
    """
    Cria uma instância do modelo Game a partir dos dados retornados pela API.

    Parameters
    ----------
    api_game : dict
        Dados do jogo retornados pela API da loteria.

    previous_game : list[int]
        Lista de números do jogo anterior. Utilizada para calcular
        estatísticas de repetição entre concursos.

    balls_map : dict[int, Ball]
        Dicionário contendo todas as bolas do banco de dados.
        A chave é o número da bola e o valor é a instância do modelo Ball.

    Returns
    -------
    tuple
        (game_object, dezenas)

        game_object : Game
            Instância do modelo Game pronta para ser inserida no banco.

        dezenas : list[int]
            Lista de números sorteados convertidos para inteiro.
    """

    # Converte os números da API (geralmente string) para inteiros
    dezenas = [int(n) for n in api_game["listaDezenas"]]

    # Cria o objeto Game com estatísticas calculadas
    game = Game(
        number=api_game["numero"],
        date=datetime.datetime.strptime(api_game["dataApuracao"], "%d/%m/%Y"),

        # Estatísticas de pares
        pairs=GameCalcData.cont_pairs(dezenas),
        sum_pairs=GameCalcData.sum_pairs(dezenas),

        # Estatísticas de ímpares
        odds=GameCalcData.cont_odds(dezenas),
        sum_odds=GameCalcData.sum_odds(dezenas),

        # Estatísticas de primos
        primes=GameCalcData.cont_primes(dezenas),
        sum_primes=GameCalcData.sum_primes(dezenas),

        # Estatísticas de Fibonacci
        fibonaccis=GameCalcData.cont_fibonaccis(dezenas),
        sum_fibonaccis=GameCalcData.sum_fibonaccis(dezenas),

        # Soma geral dos números sorteados
        sum_general=GameCalcData.sum_array(dezenas),

        # Estatísticas de números do centro
        center=GameCalcData.cont_center(dezenas),
        sum_center=GameCalcData.sum_center(dezenas),

        # Estatísticas de números da borda
        border=GameCalcData.cont_border(dezenas),
        sum_border=GameCalcData.sum_border(dezenas),

        # Estatísticas comparadas com o jogo anterior
        repeated_previous_game=GameCalcData.count_repeated_previous_game(dezenas, previous_game),
        pairs_repeated_previous_game=GameCalcData.count_pairs_repeated_previous_game(dezenas, previous_game),
        odds_repeated_previous_game=GameCalcData.count_odds_repeated_previous_game(dezenas, previous_game),
        primes_repeated_previous_game=GameCalcData.count_primes_repeated_previous_game(dezenas, previous_game),
        fibonaccis_repeated_previous_game=GameCalcData.count_fibonaccis_repeated_previous_game(dezenas, previous_game),

        center_repeated_previous_game=GameCalcData.cont_center_repeated_previous_game(dezenas, previous_game),
        border_repeated_previous_game=GameCalcData.cont_border_repeated_previous_game(dezenas, previous_game),

        # Quantidade de ganhadores por faixa
        winners_15_hits=api_game["listaRateioPremio"][0]["numeroDeGanhadores"],
        winners_14_hits=api_game["listaRateioPremio"][1]["numeroDeGanhadores"],
        winners_13_hits=api_game["listaRateioPremio"][2]["numeroDeGanhadores"],
        winners_12_hits=api_game["listaRateioPremio"][3]["numeroDeGanhadores"],
        winners_11_hits=api_game["listaRateioPremio"][4]["numeroDeGanhadores"],
    )

    # Associa as bolas sorteadas ao jogo
    for n in dezenas:
        ball = balls_map.get(n)
        if ball:
            game.drawn_balls.append(ball)

    return game, dezenas


def game_update():
    """
    Atualiza a tabela de jogos no banco de dados utilizando dados da API.

    Fluxo da função
    ----------------

    1. Busca o último jogo armazenado no banco de dados.
    2. Busca o último jogo disponível na API.
    3. Verifica se o banco está desatualizado.
    4. Caso esteja desatualizado:
        - busca todos os concursos faltantes
        - cria objetos Game
        - associa bolas
        - insere todos os jogos no banco.

    Returns
    -------
    None
    """

    with get_session() as session:

        # Busca o último jogo armazenado na base
        last_game_db = (
            session.query(Game)
            .options(joinedload(Game.drawn_balls))
            .order_by(Game.id.desc())
            .first()
        )

        # Caso a base esteja vazia
        if not last_game_db:
            print("Nenhum jogo encontrado na base.")
            return

        # Extrai os números do último jogo
        last_numbers = [ball.desc for ball in last_game_db.drawn_balls]

        # Busca o último jogo disponível na API
        last_api_game = get_game()

        # Se os números forem iguais, o banco já está atualizado
        if last_numbers == last_api_game["listaDezenas"]:
            print("Base já atualizada.")
            return

        # Cria um mapa das bolas para evitar várias queries
        balls_map = {b.desc: b for b in session.query(Ball).all()}

        # Define o intervalo de concursos que precisam ser atualizados
        start = last_game_db.number + 1
        end = last_api_game["numero"]

        print(f"Atualizando jogos {start} até {end}")

        previous = last_numbers
        new_games = []

        # Busca e processa cada concurso faltante
        for concurso in range(start, end + 1):

            api_game = get_game(concurso)

            # Atualiza tabela de bolas caso necessário
            ball_update(api_game["listaDezenas"])

            # Cria objeto Game
            game_obj, dezenas = create_game_object(api_game, previous, balls_map)

            new_games.append(game_obj)

            # Atualiza referência para o próximo loop
            previous = dezenas

        try:
            # Insere todos os jogos de uma vez
            session.add_all(new_games)
            session.commit()

            print(f"{len(new_games)} jogos inseridos com sucesso.")

        except Exception as e:
            session.rollback()
            print("Erro ao inserir jogos:", e)


if __name__ == "__main__":
    game_update()