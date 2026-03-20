from models_manipulations.game_manipulation.GameCalcdata import GameCalcData
from util.json_manipulation import save_json, load_json
import datetime
import numpy as np


def valida_game(game, quant, quant_balls=15):
    """
    Gera jogos válidos de Lotofácil baseados em regras estatísticas.

    A função cria combinações aleatórias de números entre 1 e 25 e aplica
    uma série de filtros estatísticos baseados em padrões observados em
    resultados históricos.

    Somente jogos que satisfazem TODAS as condições definidas são aceitos
    e armazenados.

    Parameters
    ----------
    quant : int
        Quantidade de jogos válidos que devem ser gerados.

    game : list
        Lista contendo os números do último jogo oficial. Essa informação
        é utilizada para calcular repetições entre o jogo gerado e o jogo anterior.

    quant_balls : int, optional
        Quantidade de números por jogo. O padrão da Lotofácil é 15.

    Returns
    -------
    list
        Lista contendo os jogos gerados que passaram em todas as validações.
        Cada jogo é representado como um numpy array ordenado.

    Observações
    ----------
    - Os jogos gerados também são salvos no arquivo JSON "My_Games".
    - Cada jogo salvo contém:
        - os números sorteados
        - a data de geração
    """

    # Lista que armazenará os jogos aprovados pelas regras
    champion_numbers = []

    # Continua gerando jogos até atingir a quantidade solicitada
    while len(champion_numbers) < int(quant):

        # Gera 15 números aleatórios entre 1 e 25 sem repetição
        numeros = np.sort(
            np.random.choice(np.arange(1, 26), size=quant_balls, replace=False)
        )

        # Lista de condições que o jogo precisa satisfazer
        conditions = [
            # Quantidade de números ímpares
            GameCalcData.cont_odds(numeros) in [7, 8],
            # Quantidade de números da borda do volante
            GameCalcData.cont_border(numeros) in [10, 9],
            # Quantidade de números do centro do volante
            GameCalcData.cont_center(numeros) in [5, 6],
            # Quantidade de números repetidos do jogo anterior
            GameCalcData.count_repeated_previous_game(numeros, game) in [8, 9, 10],
            # Quantidade de números primos
            GameCalcData.cont_primes(numeros) in [4, 5, 6, 7],
            # Quantidade de números de Fibonacci
            GameCalcData.cont_fibonaccis(numeros) in [4, 5, 6, 7],
            # Quantidade de ímpares repetidos do jogo anterior
            GameCalcData.count_odds_repeated_previous_game(numeros, game)
            in [3, 4, 5, 6],
            # Quantidade de primos repetidos do jogo anterior
            GameCalcData.count_primes_repeated_previous_game(numeros, game)
            in [2, 3, 4],
            # Quantidade de Fibonacci repetidos do jogo anterior
            GameCalcData.count_fibonaccis_repeated_previous_game(numeros, game)
            in [1, 2, 3, 4],
            # Regras de posição (distribuição dos números)
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
            numeros[14] in [24, 25],
        ]

        # Verifica se TODAS as condições são verdadeiras
        if all(conditions):

            # Adiciona o jogo aprovado à lista de jogos válidos
            champion_numbers.append(numeros)

        # Carrega jogos já existentes no arquivo JSON
        my_games = load_json("My_Games")

        # Adiciona os jogos aprovados ao arquivo
        for game_numbers in champion_numbers:
            my_games.append(
                {
                    "game": game_numbers.tolist(),  # Converte numpy array para lista
                    "date": datetime.datetime.now().isoformat(),  # Data de geração
                }
            )

        # Mostra os jogos armazenados
        # print(champion_numbers)

        # Salva os jogos atualizados no arquivo JSON
        save_json(my_games, "My_Games")

    # Retorna os jogos válidos gerados
    return champion_numbers


# Código auxiliar para debug
# Caso queira descobrir qual regra está falhando
#
# if not all(conditions):
#     for i, cond in enumerate(conditions):
#         if not cond:
#             print(f"Condição {i} falhou")
