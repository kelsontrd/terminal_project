from db.db_base import get_session
from models.Game import Game
from util.json_manipulation import save_json
import uuid


class BallCalcData:

    @staticmethod
    def analise_balls():
        """
        Realiza análise estatística das bolas da Lotofácil (1 a 25)
        com base nos jogos armazenados em base_games.json.

        Estatísticas calculadas:
        - frequency: quantidade de vezes que a bola apareceu
        - max_sequency: maior sequência de aparições consecutivas
        - current_sequency: sequência atual de aparições
        - max_delay: maior atraso entre aparições
        - current_delay: atraso atual
        """

        # Carrega todos os jogos da base
        with get_session() as session:

            # carrega jogos ordenados
            games = (
                session.query(Game)
                .order_by(Game.number.asc())
                .all()
            )

            # transforma em lista de números
            data_games = [
                [ball.desc for ball in game.drawn_balls]
                for game in games
            ]
        data_balls = []
        # Analisa cada número de 1 a 25
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

            # Percorre todos os jogos
            for game in data_games:

                # Se o número apareceu no jogo
                if i in game["drawn_numbers"]:
                    analise["frequency"] += 1
                    temp_sequency += 1
                    temp_delay = 0

                    analise["current_sequency"] = temp_sequency
                    analise["max_sequency"] = max(
                        analise["max_sequency"], temp_sequency
                    )
                    analise["current_delay"] = 0

                # Se não apareceu
                else:
                    temp_delay += 1
                    temp_sequency = 0

                    analise["current_delay"] = temp_delay
                    analise["max_delay"] = max(
                        analise["max_delay"], temp_delay
                    )
                    analise["current_sequency"] = 0

            # Monta estrutura final da bola
            data_balls.append(
                {
                    "id": str(uuid.uuid4()),
                    "num": i,
                    "pair": i % 2 == 0,

                    # verifica se é primo
                    "prime": (
                        all(i % n != 0 for n in range(2, int(i**0.5) + 1))
                        if i > 1
                        else False
                    ),

                    **analise,
                }
            )

        print(data_balls)

        # Salva análise em JSON
        save_json(data_balls, "data_nums")


if __name__ == "__main__":
    BallCalcData.analise_balls()