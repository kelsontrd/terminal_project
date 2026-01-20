from util.system_clear import clear_system

def menu_principal():
    clear_system()
    print("\n--- Menu Principal ---\n")
    print("1. Resetar ou Atualizar Base De Dados")
    print("2. -----")
    print("3. -----")
    print("4. ------")
    print("5. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        return "menu_reset_data_base"
    elif opcao == "5":
        return "sair"
    else:
        print("\n⚠️ Opção inválida!")
        input("Presione Enter para voltar ao menu...")
        return "menu_principal"