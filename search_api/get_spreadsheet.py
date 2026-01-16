import requests
import os


def get_plan(
    url="https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotof%C3%A1cil",
    file_name="lotofacil.xlsx",
):
    """
    Faz o download de uma planilha a partir de uma URL e a salva localmente.
    """
    folder_path = os.path.join(os.getcwd(), "search_api", "spreadsheets_downloads")

    try:
        file_path = os.path.join(folder_path, file_name)

        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Planilha baixada com sucesso e salva em: {file_path}")
        return file_path

    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a planilha: {e}")
        return None


# if __name__ == "__main__":
#     url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotof%C3%A1cil"
#     file_name = "lotofacil.xlsx"
#     get_plan(url, file_name)

