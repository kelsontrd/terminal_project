from db.db_base import get_session
from models.Game import Game
from sqlalchemy.orm import joinedload
import numpy as np


def search_game(user_game):
    """
    Compara um jogo informado pelo usuário com todos os jogos da base
    e retorna quantos acertos (de 11 a 15) ocorreram historicamente.

    A comparação é feita utilizando NumPy para melhorar a performance,
    transformando os jogos em uma matriz binária.

    Parâmetros
    ----------
    user_game : list[int]
        Lista contendo os números do jogo do usuário (ex: 15 números da Lotofácil).

    Retorno
    -------
    dict
        Estrutura contendo quantidade de ocorrências e concursos onde houve
        11 a 15 acertos.

        Exemplo:
        {
            "15 acertos": {
                "quantidade": 0,
                "jogos": []
            },
            "14 acertos": {...},
            ...
        }
    """

    # Abre sessão com o banco de dados
    with get_session() as session:

        # Carrega todos os jogos e suas bolas relacionadas
        # joinedload evita múltiplas consultas ao banco (N+1 problem)
        games = (
            session.query(Game)
            .options(joinedload(Game.drawn_balls))
            .order_by(Game.number.asc())
            .all()
        )

        concursos = []  # armazena os números dos concursos
        matrix = []  # matriz binária que representará os jogos

        # Converte cada jogo do banco em um vetor binário de 25 posições
        for game in games:

            # lista com os números sorteados no concurso
            balls = [ball.desc for ball in game.drawn_balls]

            # vetor de 25 posições representando as bolas (1-25)
            row = np.zeros(25, dtype=int)

            # marca 1 nas posições das bolas sorteadas
            for b in balls:
                row[b - 1] = 1

            matrix.append(row)
            concursos.append(game.number)

        # transforma lista em matriz NumPy
        matrix = np.array(matrix)

    # cria vetor binário representando o jogo do usuário
    user_vector = np.zeros(25, dtype=int)

    for n in user_game:
        user_vector[n - 1] = 1

    # produto matricial:
    # calcula quantos números coincidem entre o jogo do usuário
    # e cada jogo da base
    matches = matrix @ user_vector

    # estrutura de retorno
    result = {
        "15 acertos": {"quantidade": 0, "jogos": []},
        "14 acertos": {"quantidade": 0, "jogos": []},
        "13 acertos": {"quantidade": 0, "jogos": []},
        "12 acertos": {"quantidade": 0, "jogos": []},
        "11 acertos": {"quantidade": 0, "jogos": []},
    }

    # percorre resultados calculados pelo NumPy
    for i, m in enumerate(matches):

        # considera apenas jogos com 11 a 15 acertos
        if 11 <= m <= 15:

            key = f"{m} acertos"

            result[key]["quantidade"] += 1
            result[key]["jogos"].append({"concurso": concursos[i]})

    print(
        f"Resultados para o jogo {game}:\n"
        f"15 acertos: {result['15 acertos']['quantidade']} ocorrências\n"
        f"14 acertos: {result['14 acertos']['quantidade']} ocorrências\n"
        f"13 acertos: {result['13 acertos']['quantidade']} ocorrências\n"
        f"12 acertos: {result['12 acertos']['quantidade']} ocorrências\n"
        f"11 acertos: {result['11 acertos']['quantidade']} ocorrências\n"
    )

    return result


if __name__ == "__main__":

    # exemplo de jogo para teste
    game = [1, 3, 5, 7, 9, 10, 12, 13, 15, 16, 18, 20, 21, 23, 25]

    # result = search_game(game)

    # print(
    #     f"Resultados para o jogo {game}:\n"
    #     f"15 acertos: {result['15 acertos']['quantidade']} ocorrências\n"
    #     f"14 acertos: {result['14 acertos']['quantidade']} ocorrências\n"
    #     f"13 acertos: {result['13 acertos']['quantidade']} ocorrências\n"
    #     f"12 acertos: {result['12 acertos']['quantidade']} ocorrências\n"
    #     f"11 acertos: {result['11 acertos']['quantidade']} ocorrências\n"
    # )
