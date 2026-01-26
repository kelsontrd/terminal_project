from util.system_clear import clear_system
from extract_data.gerar_games import gerar_games
def menu_gerar_games():
    clear_system()
    print("\n--- Gerar Jogos ---\n")
    print("1. Novos Jogos")
    print("2. Ver jogos criados")
    print("3. Voltar ao menu principal")
    print("0. Sair do App")
    op = input("\nEscolha uma opção: ")
    if op == "1":
        clear_system()
        gerar_games()
        input("Presione Enter para voltar ao menu...")
        return "menu_gerar_games"
    elif op == "2":
        clear_system()
        print("Em Desenvolvimento")
        input("Presione Enter para voltar ao menu...")
        return "menu_gerar_games"
    elif op == "3":
        return "menu_principal"
    elif op == "0":
        print("👋 Saindo...")
        return "sair"
    else:
        print("\n⚠️ Opção inválida!")
        input("Presione Enter para voltar ao menu...")
        return "menu_gerar_games"