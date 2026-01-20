from db.db_create_tables import db_create_tables
from search_api.convert_spreadsheet_data_json import init
from ball_manipulation.ball_init_base import ball_init_base
from util.system_clear import clear_system



# Menu interativo no terminal
def menu():
    clear_system()
    while True:
        print("\n--- Nubers Teory System ---")
        print("1. Resetar ou Atualizar Base De Dados")
        print("2. -----")
        print("3. -----")
        print("4. ------")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            clear_system()
            print("Digite 1. Para resetar a base de dados | 2. Para atualizar a base de dados\n")
            op1 = input("Escolha uma opção: ")
            if op1 == "1":
                print("🔄 Resetando base de dados...")
                ball_init_base()
                print("✅ Base de dados resetada com sucesso!")
                input("Presione Enter para voltar ao menu...")
                menu()
        elif opcao == "2":
            input("Digite 0 para voltar ao menu: ")
            if input == "0":
                menu()
            else:
                print("⚠️ Opção inválida!")
        elif opcao == "3":
            input("Digite 0 para voltar ao menu: ")
            if input == "0":
                menu()
            else:
                print("⚠️ Opção inválida!")
        elif opcao == "4":
            input("Digite 0 para voltar ao menu: ")
            if input == "0":
                menu()
            else:
                print("⚠️ Opção inválida!")
        elif opcao == "5":
            print("👋 Saindo...")
            break
        elif opcao == "0":
           menu()
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    # Cria as tabelas no banco de dados
    db_create_tables()
    menu()
