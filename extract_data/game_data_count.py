from models.Ball import Ball
from models.Game import Game
from db.db_base import get_session
from collections import Counter
from util.json_manipulation import save_json
from sqlalchemy import or_, and_
import numpy as np


def game_pairs_count():
    with get_session() as session:
        games = session.query(Game).all()

        if games:
            result_pairs = np.array([game.pairs for game in games])
            pares_unicos, ocorrencias = np.unique(result_pairs, return_counts=True)
            lista_final_pairs = [
                {"par": int(par), "ocorrencias": int(oc)}
                for par, oc in zip(pares_unicos, ocorrencias)
            ]
            save_json(lista_final_pairs, "game_pairs_count")

            result_primes = np.array([game.primes for game in games])
            primes_unicos, ocorrencias_primes = np.unique(
                result_primes, return_counts=True
            )
            lista_final_primes = [
                {"prime": int(prime), "ocorrencias": int(oc)}
                for prime, oc in zip(primes_unicos, ocorrencias_primes)
            ]
            save_json(lista_final_primes, "game_primes_count")

            result_fibonaccis = np.array([game.fibonaccis for game in games])
            fibonaccis_unicos, ocorrencias_fibonaccis = np.unique(
                result_fibonaccis, return_counts=True
            )
            lista_final_fibonaccis = [
                {"fibonacci": int(fib), "ocorrencias": int(oc)}
                for fib, oc in zip(fibonaccis_unicos, ocorrencias_fibonaccis)
            ]
            save_json(lista_final_fibonaccis, "game_fibonaccis_count")

            result_center = np.array([game.center for game in games])
            center_unicos, ocorrencias_center = np.unique(
                result_center, return_counts=True
            )
            lista_final_center = [
                {"center": int(center), "ocorrencias": int(oc)}
                for center, oc in zip(center_unicos, ocorrencias_center)
            ]
            save_json(lista_final_center, "game_center_count")

            result_border = np.array([game.border for game in games])
            border_unicos, ocorrencias_border = np.unique(
                result_border, return_counts=True
            )
            lista_final_border = [
                {"border": int(border), "ocorrencias": int(oc)}
                for border, oc in zip(border_unicos, ocorrencias_border)
            ]
            save_json(lista_final_border, "game_border_count")

            result_count_previous = np.array([game.repeated_previous_game for game in games])
            count_previous_unicos, ocorrencias_count_previous = np.unique(
                result_count_previous, return_counts=True
            )
            lista_final_count_previous = [
                {"repeated_previous_game": int(count), "ocorrencias": int(oc)}
                for count, oc in zip(count_previous_unicos, ocorrencias_count_previous)
            ]
            save_json(lista_final_count_previous, "game_count_previous_count")

            ouro_default = (
                session.query(Game)
                .filter(
                    or_(
                        Game.odds == 8,
                        Game.odds == 7,
                    ),and_(
                        Game.border == 10,
                        Game.center == 5

                    )
                )
                .all()
            )
            ouro_default_2 = (
                session.query(Game)
                .filter(
                    or_(
                        Game.odds == 8,
                        Game.odds == 7,
                    ),and_(
                        Game.border == 9,
                        Game.center == 6

                    )
                )
                .all()
            )
            ouro_default_3 = (
                session.query(Game)
                .filter(
                    or_(
                        Game.odds == 8,
                        Game.odds == 7,
                    ),and_(
                        Game.border == 9,
                        Game.center == 6,
                        Game.fibonaccis == 4
                    )
                )
                .all()
            )
            ouro_default_4 = (
                session.query(Game)
                .filter(
                    or_(
                        Game.odds == 8,
                        Game.odds == 7,
                    ),and_(
                        Game.border == 10,
                        Game.center == 5,
                        Game.fibonaccis == 4
                    )
                )
                .all()
            )
            print(f"Ouro Default 1 (7 ou 8 impares),(10 na borda e 5 no centro)encontrado em {len(ouro_default)} jogos entre {len(games)}.")
            print(f"Ouro Default 4 (7 ou 8 impares),(10 na borda e 5 no centro e 4 fibonacci)encontrado em {len(ouro_default_4)} jogos entre {len(games)}.")
            print(f"Ouro Default 3 (7 ou 8 impares),(9 na borda e 6 no centro e 4 fibonacci)encontrado em {len(ouro_default_3)} jogos entre {len(games)}.")
            print(f"Ouro Default 2 (7 ou 8 impares),(9 na borda e 6 no centro)encontrado em {len(ouro_default_2)} jogos entre {len(games)}.")
            
            
        else:
            print("No games found in database")


if __name__ == "__main__":
    game_pairs_count()
