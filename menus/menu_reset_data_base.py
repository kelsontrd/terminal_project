from util.system_clear import clear_system
from models_manipulations.ball_manipulation.ball_init_base import ball_init_base
from models_manipulations.game_manipulation.game_init_base import game_init_base
from models_manipulations.game_manipulation.games_update.game_update import game_update
def menu_reset_data_base():
    clear_system()
    print("\n--- Resetar ou Atualizar Base De Dados ---\n")
    print("1. Resetar a base de dados")
    print("2. Atualizar a base de dados")
    print("3. Voltar ao menu principal")
    print("0. Sair do App")
    
    op = input("\nEscolha uma opção: ")
    if op == "1":
        clear_system()
        print("🔄 Resetando base de dados...")
        ball_init_base()
        game_init_base()
        print("✅ Base de dados resetada com sucesso!")
        input("Presione Enter para voltar ao menu...")
        return "menu_reset_data_base"
    elif op == "2":
        print("🔄 Atualizando base de dados...")
        game_update()
        print("✅ Base de dados atualizada com sucesso!")
        input("Presione Enter para voltar ao menu...")
        return "menu_reset_data_base"
    elif op == "3":
        return "menu_principal"
    elif op == "0":
        print("👋 Saindo...")
        return "sair"
    else:
        print("\n⚠️ Opção inválida!")
        input("Presione Enter para voltar ao menu...")
        return "menu_reset_data_base"