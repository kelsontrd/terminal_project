from util.system_clear import clear_system
from exib_data.exib_balls import exib_balls
def menu_exib_bolas():
    clear_system()
    print("\n--- BOLAS ---\n")
    print("1. Exibir todas as bolas")
    print("2. Buscar bola por numero")
    print("3. Voltar ao menu principal")
    print("0. Sair do App")
    
    op = input("\nEscolha uma opção: ")
    if op == "1":
        clear_system()
        print("🔄 Carregando todas as bolas...\n")
        exib_balls()
        input("Presione Enter para voltar ao menu...")
        return "menu_exib_bolas"
    elif op == "2":
        clear_system()
        input_num = input("Digite o número da bola que deseja buscar: ")
        print("🔄Exibindo bola selecionada...")
        exib_balls(input_num)
        input("Presione Enter para voltar ao menu...")
        return "menu_exib_bolas"
    elif op == "3":
        return "menu_principal"
    elif op == "0":
        print("👋 Saindo...")
        return "sair"
    else:
        print("\n⚠️ Opção inválida!")
        input("Presione Enter para voltar ao menu...")
        return "menu_reset_data_base"