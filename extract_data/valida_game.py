from models_manipulations.game_manipulation.GameCalcdata import GameCalcData
from util.json_manipulation import save_json, load_json
import datetime
import numpy as np
def valida_game(quant, game):
    champion_numbers = []
    while len(champion_numbers) < int(quant):
        # print(len(champion_numbers))
        numeros = np.sort(np.random.choice(np.arange(1, 26), size=15, replace=False))
        conditions = [
            GameCalcData.cont_odds(numeros) in [7, 8],
            GameCalcData.cont_border(numeros) in [10, 9],
            GameCalcData.cont_center(numeros) in [5, 6],
            GameCalcData.count_repeated_previous_game(numeros, game) in [8, 9, 10],
            GameCalcData.cont_primes(numeros) in [4, 5, 6, 7],
            GameCalcData.cont_fibonaccis(numeros) in [4, 5, 6, 7],
            GameCalcData.count_odds_repeated_previous_game(numeros, game) in [3,4,5,6],
            GameCalcData.count_primes_repeated_previous_game(numeros, game) in [2,3,4],
            GameCalcData.count_fibonaccis_repeated_previous_game(numeros, game) in [1,2,3,4],
            numeros[0] in [1, 2],
            numeros[1] in [2, 3, 4],
            numeros[2] in [3, 4, 5, 6],
            numeros[3] in [5, 6, 7, 8],
            numeros[4] in [6, 7, 8, 9, 10],
            numeros[5] in [8, 9, 10, 11],
            numeros[6] in [10, 11, 12, 13],
            numeros[7] in [11, 12, 13, 14, 15],
            numeros[8] in [13, 14, 15, 16, 17],
            numeros[9] in [15, 16, 17, 18],
            numeros[10] in [17, 18, 19, 20],
            numeros[11] in [18, 19, 20, 21],
            numeros[12] in [20, 21, 22, 23],
            numeros[13] in [22, 23, 24],
            numeros[14] in [24, 25]
        ]
        # Se TODAS as condições forem verdadeiras
        if all(conditions):
            champion_numbers.append(numeros)
        my_games = load_json("My_Games")
        for i in range(len(champion_numbers)+1):
            my_games.append({
            "game": champion_numbers[i],
            "date": datetime.datetime.now()
        })
        print(my_games)
        save_json(my_games, "My_Games")
    return champion_numbers

#para debug
# if not all(conditions):
#     # Mostra quais condições falharam
#     for i, cond in enumerate(conditions):
#         if not cond:
#             print(f"Condição {i} falhou")