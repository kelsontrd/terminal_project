from db.db_create_tables import db_create_tables
from menus.menu_reset_data_base import menu_reset_data_base
from menus.menu_principal import menu_principal

# Menu interativo no terminal
def app():
    state = "menu_principal"
    while state != "sair":
        if state == "menu_principal":
            state = menu_principal()
        if state == "menu_reset_data_base":
            state = menu_reset_data_base()
        elif state == "sair":
            print("👋 Saindo...")

if __name__ == "__main__":
    # Cria as tabelas no banco de dados
    db_create_tables()
    app()
