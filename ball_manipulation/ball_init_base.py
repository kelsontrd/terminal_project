from util.json_manipulation import load_json

def ball_init_base():
    data_balls = load_json("base_games")
    print(data_balls)
    balls = []
    for i in range(1, 26):
        frequency = 0
        current_sequency = 0
        max_sequency = 0
        current_delay = 0
        max_delay = 0
    
        for game in data_balls:
            if i in game["drawn_numbers"]:
                frequency += 1
                current_sequency += 1
                if current_sequency > max_sequency:
                    max_sequency = current_sequency
                current_delay = 0
            else:
                current_sequency = 0
                current_delay += 1
                if current_delay > max_delay:
                    max_delay = current_delay
                
                
