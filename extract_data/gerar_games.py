from models_manipulations.game_manipulation.games_update.get_game_api import get_game
from models_manipulations.game_manipulation.search_game import search_game
from extract_data.valida_game import valida_game


def gerar_games():

    last_game_api = get_game()
    last_game = last_game_api["listaDezenas"]

    quant = 0
    while quant == 0:
        quant = input("Digite a quantidade de jogos a criar:\n")
        quant_balls = int(input("Digite a quantidade de números por jogo (padrão é 15):\n"))
        if quant == 0 or quant_balls < 15 or quant_balls == "":
            print(
                f"Parametros incorretos jogos dever ser maior qque 0 \n e quantidade de bolas deve ser maior ou igual a 15"
            )

    print("Gerando Jogos...")
    if quant_balls > 15:
        champions_games = valida_game(last_game, quant,  quant_balls)
    else:
        champions_games = valida_game(last_game, quant,)
    print("Jogos gerado com sucesso!", end="\r")
    for game in champions_games:
        print(game)
        search_game(game)
    return


if __name__ == "__main__":
    gerar_games()
