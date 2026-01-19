import numpy as np
import math

# Classe para calcular diversos dados sobre os jogos, toda informação que será preciso calcular
# será feito aqui, como soma, média, mediana, etc.
class Calc_data:
    @staticmethod
    def set_array_integer(numbers):
        return np.array(numbers, dtype=int)
    # Pares
    @staticmethod
    def cont_pairs(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.count_nonzero(arr % 2 == 0)

    @staticmethod
    def sum_pairs(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.sum(arr[arr % 2 == 0])

    # Ímpares
    @staticmethod
    def cont_odds(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.count_nonzero(arr % 2 != 0)

    @staticmethod
    def sum_odds(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.sum(arr[arr % 2 != 0])

    # Primos
    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def cont_primes(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.count_nonzero([Calc_data.is_prime(n) for n in arr])

    @staticmethod
    def sum_primes(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.sum([n for n in arr if Calc_data.is_prime(n)])

    # Soma geral
    @staticmethod
    def sum_array(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.sum(arr)

    # Centro e borda
    @staticmethod
    def sum_center(numbers):
        arr = Calc_data.set_array_integer(numbers)
        center = np.array([7,8,9,12,13,14,17,18,19], dtype=int)
        return np.intersect1d(center, arr).size

    @staticmethod
    def sum_border(numbers):
        arr = Calc_data.set_array_integer(numbers)
        border = np.array([1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25], dtype=int)
        return np.intersect1d(border, arr).size

    # Fibonacci
    @staticmethod
    def is_fibonacci(n):
        def is_perfect_square(x):
            s = int(math.sqrt(x))
            return s * s == x
        return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

    @staticmethod
    def cont_fibonaccis(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.count_nonzero([Calc_data.is_fibonacci(n) for n in arr])

    @staticmethod
    def sum_fibonaccis(numbers):
        arr = Calc_data.set_array_integer(numbers)
        return np.sum([n for n in arr if Calc_data.is_fibonacci(n)])

    # Comparações com jogo anterior
    @staticmethod
    def count_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0
        try:
            arr1 = Calc_data.set_array_integer(numbers)
            arr2 = Calc_data.set_array_integer(previous)
            return np.intersect1d(arr1, arr2).size
        except:
            print(f"Erro ao comparar com jogo anterior: numbers={numbers}, previous={previous} in Calc_data.count_repeated_previous_game")
            return None

    @staticmethod
    def count_pairs_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = Calc_data.set_array_integer(numbers)
            arr2 = Calc_data.set_array_integer(previous)
            arr2_pairs = arr2[arr2 % 2 == 0]
            return np.intersect1d(arr1, arr2_pairs).size
        except:
            print(f"Erro ao comparar pares com jogo anterior: numbers={numbers}, previous={previous} in Calc_data.count_pairs_repeated_previous_game")
            return None

    @staticmethod
    def count_odds_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = Calc_data.set_array_integer(numbers)
            arr2 = Calc_data.set_array_integer(previous)
            arr2_odds = arr2[arr2 % 2 != 0]
            return np.intersect1d(arr1, arr2_odds).size
        except:
            print(f"Erro ao comparar ímpares com jogo anterior: numbers={numbers}, previous={previous} in Calc_data.count_odds_repeated_previous_game")
            return None

    @staticmethod
    def count_primes_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = Calc_data.set_array_integer(numbers)
            arr2 = Calc_data.set_array_integer(previous)
            arr2_primes = [n for n in arr2 if Calc_data.is_prime(n)]
            return np.intersect1d(arr1, arr2_primes).size
        except:
            print(f"Erro ao comparar primos com jogo anterior: numbers={numbers}, previous={previous} in Calc_data.count_primes_repeated_previous_game")
            return None

    @staticmethod
    def count_fibonaccis_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = Calc_data.set_array_integer(numbers)
            arr2 = Calc_data.set_array_integer(previous)
            arr2_fibs = [n for n in arr2 if Calc_data.is_fibonacci(n)]
            return np.intersect1d(arr1, arr2_fibs).size
        except:
            print(f"Erro ao comparar Fibonacci com jogo anterior: numbers={numbers}, previous={previous} in Calc_data.count_fibonaccis_repeated_previous_game")
            return None    
