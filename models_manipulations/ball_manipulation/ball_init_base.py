from util.json_manipulation import load_json
from models.Ball import Ball
from db.db_base import session
from sqlalchemy import delete
from search_api.convert_spreadsheet_data_json import init

def ball_init_base():
    #init() # inicializa o arquivo base_games.json a partir da planilha atualizada completa alterar para teste
    data_balls = load_json("base_games")
    balls = []
    
    for i in range(1, 26):
        frequency = 0
        current_sequence = 0
        max_sequence = 0
        current_delay = 0
        max_delay = 0

        for game in data_balls:
            if i in game["drawn_numbers"]:
                frequency += 1
                current_sequence += 1
                if current_sequence > max_sequence:
                    max_sequence = current_sequence
                current_delay = 0
            else:
                current_sequence = 0
                current_delay += 1
                if current_delay > max_delay:
                    max_delay = current_delay
        balls.append(
            Ball(
                desc=i,
                frequency=frequency,
                currente_sequence=current_sequence,
                max_sequence=max_sequence,
                currente_delay=current_delay,
                max_delay=max_delay,
            )
        )
        
        # sys.stdout.write(f"\Inserindo Bola numero: {i}%") # j*4 para mostrar o progresso de 4 em 4%
        # sys.stdout.flush() # necessário para atualizar o progresso no terminal
        # time.sleep(0.05) # para não sobrecarregar o terminal com atualizações
    try:
        # session.bulk_insert_mappings(Ball, balls)
        session.execute(delete(Ball))  # Clear existing data
        session.add_all(balls)
        session.commit()
        print("Balls inseridas com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir bolas: {e}")
        session.rollback()
