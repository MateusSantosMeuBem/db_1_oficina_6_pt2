from main.model import connector
from main.services.database import (
    create_super_user,
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
    show_books_over_1_author,
    show_books_rating_over_3,
    show_sells_by_year,
    show_sold_books_by_id,
    show_sections,
    show_books_where_author_has
]

try:
    print('Trying conecting...')
    connection = connector()
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

except Exception as exception:
    print(exception)


