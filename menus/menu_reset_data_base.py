from util.system_clear import clear_system
from ball_manipulation.ball_init_base import ball_init_base
def menu_reset_data_base():
    clear_system()
    print("--- Resetar ou Atualizar Base De Dados ---")
    print("1. Resetar a base de dados")
    print("2. Atualizar a base de dados")
    print("3. Voltar ao menu principal")
    
    op = input("Escolha uma opção: ")
    if op == "1":
        print("🔄 Resetando base de dados...")
        ball_init_base()
        print("✅ Base de dados resetada com sucesso!")
        input("Presione Enter para voltar ao menu...")
        return "menu_reset_data_base"
    elif op == "2":
        print("🔄 Atualizando base de dados...")
        #ball_init_base()
        print("✅ Base de dados atualizada com sucesso!")
        input("Presione Enter para voltar ao menu...")
        return "menu_reset_data_base"
    elif op == "3":
        return "menu_principal"
    else:
        print("\n⚠️ Opção inválida!")
        input("Presione Enter para voltar ao menu...")
        return "menu_reset_data_base"