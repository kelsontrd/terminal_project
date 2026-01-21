from util.json_manipulation import load_json, save_json

class BallCalcData:
    
    def analise_balls():

        data_games = load_json("base_games")
        print(data_games)
        data_balls = []
        

        for i in range(1, 26):
            analise = {
                "frequency": 0,
                "max_sequency": 0,
                "current_sequency": 0,
                "max_delay": 0,
                "current_delay": 0,
            }

            temp_sequency = 0
            temp_delay = 0

            for game in data_games:

                if i in game["drawn_numbers"]:
                    analise["frequency"] += 1
                    temp_sequency += 1
                    temp_delay = 0
                    analise["current_sequency"] = temp_sequency
                    analise["max_sequency"] = max(analise["max_sequency"], temp_sequency)
                    analise["current_delay"] = 0
                    
                else:
                    temp_delay += 1
                    temp_sequency = 0
                    analise["current_delay"] = temp_delay
                    analise["max_delay"] = max(analise["max_delay"], temp_delay)
                    analise["current_sequency"] = 0

            data_nums.append(
                {
                    "id": str(uuid.uuid4()),
                    "num": i,
                    "pair": i % 2 == 0,
                    "prime": (
                        all(i % n != 0 for n in range(2, int(i**0.5) + 1))
                        if i > 1
                        else False
                    ),
                    **analise
                }
            )

        print(data_nums)
        save_json(data_nums, "data_nums")


    if __name__ == "__main__":
        analise_nuns()
