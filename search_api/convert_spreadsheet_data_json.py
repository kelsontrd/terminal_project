import pandas as pd
import uuid
import json
import os
from datetime import datetime
from search_api.get_spreadsheet import get_plan
from util.system_clear import clear_system
import time


def format_date(date):
    """Formata dados para o padrão 'DD/MM/YYYY'."""
    if pd.isna(date):
        return ""
    elif hasattr(date, "strftime"):
        return date.strftime("%d/%m/%Y")
    else:
        try:
            if isinstance(date, str):
                # Tenta diferentes formatos de data
                formatos = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%d/%m/%y"]
                for fmt in formatos:
                    try:
                        data_obj = datetime.strptime(date, fmt)
                        return data_obj.strftime("%d/%m/%Y")
                    except:
                        continue
            return str(date)
        except:
            return str(date)


def extract_data_from_excel(
    file_path=os.path.join(
        os.getcwd(), "search_api", "spreadsheets_downloads", "lotofacil.xlsx"
    )
):
    """Extrai dados de uma planilha Excel e os converte em uma lista de dicionários JSON."""
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None

    results = []

    for _, row in df.iterrows():
        try:
            draw_nums = []
            for i in range(1, 16):
                # CORREÇÃO: Removido 'ball=' que estava causando erro
                draw_nums.append(int(row[f"Bola{i}"]))

            reg = {
                "id": str(uuid.uuid4()),  # CORREÇÃO: Converter para string
                "concurso": int(row["Concurso"]),
                "data": format_date(row["Data Sorteio"]),
                "winners_15_hits": int(row["Ganhadores 15 acertos"]),
                "winners_14_hits": int(row["Ganhadores 14 acertos"]),
                "winners_13_hits": int(row["Ganhadores 13 acertos"]),
                "winners_12_hits": int(row["Ganhadores 12 acertos"]),
                "winners_11_hits": int(row["Ganhadores 11 acertos"]),
                "drawn_numbers": draw_nums,
            }

            results.append(reg)
        except Exception as e:
            print(
                f"Erro ao processar linha {row['Concurso']}: {e}"
            )  # CORREÇÃO: Mostrar o erro

    return results


def save_data():
    # CORREÇÃO: Criar pasta se não existir
    json_dir = os.path.join(os.getcwd(), "search_api", "data_jsons")
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)
        print(f"📁 Pasta criada: {json_dir}")

    # CORREÇÃO: Sintaxe das strings formatadas
    base_games = f"base_games.json"
    json_path = os.path.join(json_dir, base_games)

    dados = extract_data_from_excel()

    if dados is None:
        print("❌ Nenhum dado foi extraído da planilha!")
        return

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    clear_system()
    print(f"✅ Arquivo JSON criado com sucesso!")
    time.sleep(1)
    print(f"📁 Caminho: {json_path}")
    time.sleep(1)
    print(f"📄 Arquivo: {base_games}")
    time.sleep(1)
    print(f"📊 Total de registros: {len(dados)}")


# Adicionar para executar o script
# if __name__ == "__main__":
#     get_plan()
#     save_data()
def init():
    get_plan()
    save_data()
