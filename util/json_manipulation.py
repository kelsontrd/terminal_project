import json
import os

def load_json(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'search_api', 'data_jsons', f'{file_name}.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: O arquivo {file_path} não foi encontrado!")
        return None
    
def save_json(data, file_name):
    file_path = os.path.join(os.getcwd(), "data_jsons", f"{file_name}.json")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo {file_path}: {e}")