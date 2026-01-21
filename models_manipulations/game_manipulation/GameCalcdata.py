import numpy as np
import math

# Classe para calcular diversos dados sobre os jogos, toda informação que será preciso calcular
# será feito aqui, como soma, média, mediana, etc.
class GameCalcData:
    @staticmethod
    def set_array_integer(numbers):
        return np.array(numbers, dtype=int)
    # Pares
    @staticmethod
    def cont_pairs(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        return np.count_nonzero(arr % 2 == 0)

    @staticmethod
    def sum_pairs(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        return np.sum(arr[arr % 2 == 0])

    # Ímpares
    @staticmethod
    def cont_odds(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        return np.count_nonzero(arr % 2 != 0)

    @staticmethod
    def sum_odds(numbers):
        arr = GameCalcData.set_array_integer(numbers)
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
        arr = GameCalcData.set_array_integer(numbers)
        return np.count_nonzero([GameCalcData.is_prime(n) for n in arr])

    @staticmethod
    def sum_primes(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        return np.sum([n for n in arr if GameCalcData.is_prime(n)])

    # Soma geral
    @staticmethod
    def sum_array(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        return np.sum(arr)

    # Centro e borda
    @staticmethod
    def cont_center(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        center = np.array([7,8,9,12,13,14,17,18,19], dtype=int)
        return np.intersect1d(center, arr).size
    
    @staticmethod
    def sum_center(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        center = np.array([7,8,9,12,13,14,17,18,19], dtype=int)
        return np.intersect1d(center, arr).sum()

    #Conta numeros da borda da cartela
    @staticmethod
    def cont_border(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        border = np.array([1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25], dtype=int)
        return np.intersect1d(border, arr).size
    
    #Soma numeros da borda da cartela
    @staticmethod
    def sum_border(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        border = np.array([1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25], dtype=int)
        return np.intersect1d(border, arr).sum()

    # Fibonacci
    @staticmethod
    def is_fibonacci(n):
        def is_perfect_square(x):
            s = int(math.sqrt(x))
            return s * s == x
        return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

    # Contagem de Fibonaccis
    @staticmethod
    def cont_fibonaccis(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        return np.count_nonzero([GameCalcData.is_fibonacci(n) for n in arr])

    # Soma de todos os Fibonaccis
    @staticmethod
    def sum_fibonaccis(numbers):
        arr = GameCalcData.set_array_integer(numbers)
        return np.sum([n for n in arr if GameCalcData.is_fibonacci(n)])

    # Numeros repetidos do jogo anterior
    @staticmethod
    def count_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0
        try:
            arr1 = GameCalcData.set_array_integer(numbers)
            arr2 = GameCalcData.set_array_integer(previous)
            return np.intersect1d(arr1, arr2).size
        except:
            print(f"Erro ao comparar com jogo anterior: numbers={numbers}, previous={previous} in GameCalcData.count_repeated_previous_game")
            return None
    
    # Numeros Pares repetidos do jogo anterior por categoria
    @staticmethod
    def count_pairs_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = GameCalcData.set_array_integer(numbers)
            arr2 = GameCalcData.set_array_integer(previous)
            arr2_pairs = arr2[arr2 % 2 == 0]
            return np.intersect1d(arr1, arr2_pairs).size
        except:
            print(f"Erro ao comparar pares com jogo anterior: numbers={numbers}, previous={previous} in GameCalcData.count_pairs_repeated_previous_game")
            return None

    @staticmethod
    def count_odds_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = GameCalcData.set_array_integer(numbers)
            arr2 = GameCalcData.set_array_integer(previous)
            arr2_odds = arr2[arr2 % 2 != 0]
            return np.intersect1d(arr1, arr2_odds).size
        except:
            print(f"Erro ao comparar ímpares com jogo anterior: numbers={numbers}, previous={previous} in GameCalcData.count_odds_repeated_previous_game")
            return None

    @staticmethod
    def count_primes_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = GameCalcData.set_array_integer(numbers)
            arr2 = GameCalcData.set_array_integer(previous)
            arr2_primes = [n for n in arr2 if GameCalcData.is_prime(n)]
            return np.intersect1d(arr1, arr2_primes).size
        except:
            print(f"Erro ao comparar primos com jogo anterior: numbers={numbers}, previous={previous} in GameCalcData.count_primes_repeated_previous_game")
            return None

    @staticmethod
    def count_fibonaccis_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = GameCalcData.set_array_integer(numbers)
            arr2 = GameCalcData.set_array_integer(previous)
            arr2_fibs = [n for n in arr2 if GameCalcData.is_fibonacci(n)]
            return np.intersect1d(arr1, arr2_fibs).size
        except:
            print(f"Erro ao comparar Fibonacci com jogo anterior: numbers={numbers}, previous={previous} in GameCalcData.count_fibonaccis_repeated_previous_game")
            return None  

    # Numero repetidos do centro da cartela no jogo anterior
    @staticmethod
    def cont_center_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = GameCalcData.set_array_integer(numbers)
            arr2 = GameCalcData.set_array_integer(previous)
            center = np.array([7,8,9,12,13,14,17,18,19], dtype=int)
            arr2_center = np.intersect1d(arr2, center)
            return np.intersect1d(arr1, arr2_center).size
        except:
            print(f"Erro ao comparar centro com jogo anterior: numbers={numbers}, previous={previous} in GameCalcData.count_center_repeated_previous_game")
            return None  
        
    @staticmethod
    def cont_border_repeated_previous_game(numbers, previous):
        if previous is None:
            return 0    
        try:
            arr1 = GameCalcData.set_array_integer(numbers)
            arr2 = GameCalcData.set_array_integer(previous)
            border = np.array([1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25], dtype=int)
            arr2_border = np.intersect1d(arr2, border)
            return np.intersect1d(arr1, arr2_border).size
        except:
            print(f"Erro ao comparar borda com jogo anterior: numbers={numbers}, previous={previous} in GameCalcData.count_border_repeated_previous_game")
            return None
