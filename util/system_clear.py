import os

def clear_system():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print('Sistema operacional não suportado para alguns recursos do applicativo.')
        return