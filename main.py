from sqlalchemy.orm import sessionmaker
from db.db_base import session
from models.Tarefa import Tarefa
from db.db_create_tables import db_create_tables
from search_api.convert_spreadsheet_data_json import init


# Funções CRUD
def criar_tarefa(titulo, descricao=""):
    tarefa = Tarefa(titulo=titulo, descricao=descricao)
    session.add(tarefa)
    session.commit()
    print("✅ Tarefa criada com sucesso!")

def listar_tarefas():
    tarefas = session.query(Tarefa).all()
    print("\n📋 Lista de Tarefas:")
    for t in tarefas:
        print(f"{t.id} - {t.titulo} ({t.descricao})")

def atualizar_tarefa(id, novo_titulo=None, nova_descricao=None):
    tarefa = session.query(Tarefa).filter_by(id=id).first()
    if tarefa:
        if novo_titulo:
            tarefa.titulo = novo_titulo
        if nova_descricao:
            tarefa.descricao = nova_descricao
        session.commit()
        print("✏️ Tarefa atualizada!")
    else:
        print("⚠️ Tarefa não encontrada.")

def deletar_tarefa(id):
    tarefa = session.query(Tarefa).filter_by(id=id).first()
    if tarefa:
        session.delete(tarefa)
        session.commit()
        print("🗑️ Tarefa deletada!")
    else:
        print("⚠️ Tarefa não encontrada.")

# Menu interativo no terminal
def menu():
    while True:
        print("\n--- ToDo List ---")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Atualizar tarefa")
        print("4. Deletar tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            criar_tarefa(titulo, descricao)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            id = int(input("ID da tarefa: "))
            novo_titulo = input("Novo título (ou Enter para manter): ")
            nova_descricao = input("Nova descrição (ou Enter para manter): ")
            atualizar_tarefa(id, novo_titulo or None, nova_descricao or None)
        elif opcao == "4":
            id = int(input("ID da tarefa: "))
            deletar_tarefa(id)
        elif opcao == "5":
            print("👋 Saindo...")
            break
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    # Cria as tabelas no banco de dados
    db_create_tables()
    init()
    menu()
