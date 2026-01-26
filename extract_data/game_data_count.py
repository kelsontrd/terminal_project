from models.Ball import Ball
from models.Game import Game
from db.db_base import get_session
from collections import Counter
from util.json_manipulation import save_json
from sqlalchemy import or_, and_
import numpy as np


def game_data_count():
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
            
            result_count_previous = np.array([game.odds_repeated_previous_game for game in games])
            count_previous_unicos, ocorrencias_count_previous = np.unique(
                result_count_previous, return_counts=True
            )
            lista_final_odds_repeated_previous_game = [
                {"odds_repeated_previous_game": int(count), "ocorrencias": int(oc)}
                for count, oc in zip(count_previous_unicos, ocorrencias_count_previous)
            ]
            save_json( lista_final_odds_repeated_previous_game, " game_odds_repeated_previous_game")
            
            result_count_previous = np.array([game.primes_repeated_previous_game for game in games])
            count_previous_unicos, ocorrencias_count_previous = np.unique(
                result_count_previous, return_counts=True
            )
            lista_primes_repeated_previous_game = [
                {"odds_repeated_previous_game": int(count), "ocorrencias": int(oc)}
                for count, oc in zip(count_previous_unicos, ocorrencias_count_previous)
            ]
            save_json( lista_primes_repeated_previous_game, "game.primes_repeated_previous_game")
            
            result_count_previous = np.array([game.fibonaccis_repeated_previous_game for game in games])
            count_previous_unicos, ocorrencias_count_previous = np.unique(
                result_count_previous, return_counts=True
            )
            lista_fibonaccis_repeated_previous_game = [
                {"fibonaccis_repeated_previous_game": int(count), "ocorrencias": int(oc)}
                for count, oc in zip(count_previous_unicos, ocorrencias_count_previous)
            ]
            save_json( lista_fibonaccis_repeated_previous_game, "game.fibonaccis_repeated_previous_game")
            
        else:
            print("No games found in database")


if __name__ == "__main__":
    game_data_count()
