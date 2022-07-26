from main.model import connector
from main.services.database import (
    create_super_user,
    create_user,
    show_books_over_1_author,
    show_books_rating_over_3,
    show_sells_by_year,
    show_sold_books_by_id,
    show_sections,
    show_books_where_author_has
)

from main.utils import (
    draw_menu,
    options
)

manager = [
    create_super_user,
    create_user,
    show_books_over_1_author,
    show_books_rating_over_3,
    show_sells_by_year,
    show_sold_books_by_id,
    show_sections,
    show_books_where_author_has
]

try:
    from getpass import getpass

    db_user: str = input('Digite o nome do usuário: ')
    pass_01: str = getpass('Digite a senha do usuário: ')
    pass_02: str = getpass('Digite a senha novamente: ')

    if pass_01 == pass_02:

        print('Trying conecting...')
        connection = connector(
            db_user = db_user,
            senha_usuario_sgbd = pass_01
        )
        del db_user, pass_01, pass_02
        print('Conected!')

        while True:
            choice = draw_menu()
            if choice in [str(option) for option in range(1, len(manager) + 2)]:
                if choice == str(len(options)):
                    break
                else:
                    manager[int(choice) - 1](connection)
            else:
                print('\n -- DIGITE UMA OPÇÃO VÁLIDA -- \n')

        connection.close()
        print('Connection closed!')
    else:
        raise Exception('A senhas não são iguais!')

except Exception as exception:
    print(exception)


