from models_manipulations.game_manipulation.games_update.get_game_api import get_game
from extract_data.valida_game import valida_game

def gerar_games():
    
    last_game_api = get_game()
    last_game = last_game_api["listaDezenas"]
    
    quant = 0
    while quant == 0:
        quant = input("Digite a quantidade de jogos a criar:\n")
        if(quant == 0):
            print(f"A quantidade de jogosn não pode ser {quant}")
    
    print("Gerando Jogos...")        
    champions_games = valida_game(quant, last_game)  
    print("Jogos gerado com sucesso!", end='\r')
    for game in champions_games:
        print(game)
    return
if __name__ == "__main__":
    gerar_games()
