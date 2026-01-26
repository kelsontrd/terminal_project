import numpy as np
from models_manipulations.game_manipulation.GameCalcdata import GameCalcData
from db.db_base import get_session
from models.Ball import Ball
from models.Game import Game
from sqlalchemy.orm import joinedload
from models_manipulations.game_manipulation.games_update.get_game_api import get_game
import time


def gerar_games():
    game_in_base = get_game()
    last_game_in_base = game_in_base["listaDezenas"]
    # gera 15 números únicos entre 1 e 25
    champion_numbers = []
    # print("Último jogo na base:", last_game_in_base)

    while len(champion_numbers) < 3:
        # print(len(champion_numbers))
        numeros = np.sort(np.random.choice(np.arange(1, 26), size=15, replace=False))
        # print(numeros)
        time.sleep(0.1)
        if GameCalcData.cont_odds(numeros) in [7, 8]:
            # print("entrou impares")
            if GameCalcData.cont_border(numeros) in [10, 9]:
                # print("entrou border")
                if GameCalcData.cont_center(numeros) in [5, 6]:
                    # print("entrou center")
                    # print(int(GameCalcData.count_repeated_previous_game(numeros, last_game_in_base)))
                    if GameCalcData.count_repeated_previous_game(
                        numeros, last_game_in_base
                    ) in [8, 9, 10]:
                        # print("entrou repetidos")
                        if GameCalcData.cont_primes(numeros) in [4, 5, 6, 7]:
                            # print("entrou primos")
                            if GameCalcData.cont_fibonaccis(numeros) in [4, 5, 6, 7]:
                                # print("entrou fibonaccis")
                                champion_numbers.append(numeros)
    print(champion_numbers)


if __name__ == "__main__":
    gerar_games()
