from util.json_manipulation import load_json
from models.Game import Game
from db.db_base import session
from sqlalchemy import delete
from search_api.convert_spreadsheet_data_json import init
import sys
import time
from util.system_clear import clear_system
def game_init_base():
    
    data_games = load_json("base_games")
    games = []
    status = ""