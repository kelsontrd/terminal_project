from util.json_manipulation import load_json
from models.Ball import Ball
from db.db_base import session
from sqlalchemy import delete
from search_api.convert_spreadsheet_data_json import init
import sys
import time
from util.system_clear import clear_system


def ball_init_base():
    init()
    data_balls = load_json("base_games")
    balls = []
    status = ""
    
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
        
        for j in range(i): # \r volta o cursor para o início da linha 
            sys.stdout.write(f"\rProgresso: {i}%") 
            sys.stdout.flush()
            time.sleep(0.05)
    try:
        # session.bulk_insert_mappings(Ball, balls)
        session.execute(delete(Ball))  # Clear existing data
        session.add_all(balls)
        session.commit()
        print("Balls inserted successfully.")
    except Exception as e:
        print(f"Error inserting balls: {e}")
        session.rollback()
