options = [
    'Criar <todopoderoso>',
    'Mostrar livros com mais de 1 autor',
    'Mostrar livros com mais de 3 estrelas',
    'Mostrar livros vendidos no ano',
    'Mostrar livros vendidos pelo ID',
    'Mostrar seções',
    'Mostar livros cujo autor tenha [...]',
    'Sair'
]

def draw_menu():
    print('--------- MENU ---------')
    for key, option in enumerate(options):
        print(f'[{key + 1}] - {option}')
    print()

    return input('Opção: ')

