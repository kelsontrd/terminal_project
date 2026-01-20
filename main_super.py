from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import clear

# Simulações
def db_create_tables():
    pass

def ball_init_base():
    pass


# ---------- Submenu ----------
def menu_base_dados():
    completer = WordCompleter(["1", "2", "0"], ignore_case=True)

    while True:
        clear()
        print("\n--- Base de Dados ---")
        print("1. Resetar base de dados")
        print("2. Atualizar base de dados")
        print("0. Voltar ao menu principal")

        op = prompt("Escolha: ", completer=completer)

        if op == "1":
            print("\n🔄 Resetando base de dados...")
            ball_init_base()
            print("✅ Base de dados resetada!")
            prompt("\nPressione Enter para continuar...")

        elif op == "2":
            print("\n🔄 Atualizando base de dados...")
            prompt("\nPressione Enter para continuar...")

        elif op == "0":
            return  # volta para o menu principal

        else:
            print("\n⚠️ Opção inválida!")
            prompt("Pressione Enter...")


# ---------- Menu Principal ----------
def menu_principal():
    completer = WordCompleter(
        ["1", "2", "3", "4", "5"],
        ignore_case=True
    )

    while True:
        clear()
        print("\n--- Nubers Theory System ---")
        print("1. Resetar ou Atualizar Base De Dados")
        print("2. -----")
        print("3. -----")
        print("4. -----")
        print("5. Sair")

        op = prompt("Escolha: ", completer=completer)

        if op == "1":
            menu_base_dados()

        elif op in {"2", "3", "4"}:
            print("\n🚧 Em desenvolvimento...")
            prompt("Pressione Enter para voltar...")

        elif op == "5":
            print("\n👋 Saindo...")
            break

        else:
            print("\n⚠️ Opção inválida!")
            prompt("Pressione Enter...")


# ---------- Main ----------
if __name__ == "__main__":
    db_create_tables()
    menu_principal()
