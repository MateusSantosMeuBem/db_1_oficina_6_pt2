# 2_1 - Ítala
def show_sells_by_year(
    conexao
):
    ano = input('Ano da Venda: ')

    codigoSQL = "select codigo, data_pedido, (select cliente.nome from cliente where venda.cod_cliente = cliente.codigo) " \
                "as cliente from venda where year(data_pedido) = " + ano
    consulta = conexao.cursor()
    consulta.execute(codigoSQL)
    for c, n , a in consulta:
        print(c, n, a)

    consulta.close()

# 2_2 - Newdon
def show_books_rating_over_3(
    conexao
):
    codigoSQL = "select livro.codigo, livro.titulo, avg(estrelas_avaliacao) as media from livro, livro_venda " \
			"where livro.codigo = livro_venda.cod_livro group by livro.codigo having media > 3;"
    consulta = conexao.cursor()
    consulta.execute(codigoSQL)
    for c, n , a in consulta:
        print(c, n, a)

    consulta.close()

# 2_3 - Linda
def show_books_over_1_author(
    conexao
):
    codigoSQL = "select cod_livro, (select livro.titulo from livro where autor_livro.cod_livro = livro.codigo) " \
			"as titulo, count(cod_autor) as qtd_autor from autor_livro group by cod_livro having qtd_autor > 1 " \
			"order by qtd_autor"
    consulta = conexao.cursor()
    consulta.execute(codigoSQL)
    for cod, data, nome in consulta:
        print(cod, data, nome)
    consulta.close()

# 2_4 - Elian
def show_books_where_author_has(
    conexao
):
    termo = str(input('Digite o termo a ser encontrado no nome do autor: '))

    codSQL = "SELECT livro.titulo AS titulo_livro FROM livro, autor, autor_livro WHERE autor.nome LIKE '%"+termo+"%' AND autor.codigo = autor_livro.cod_autor AND livro.codigo = autor_livro.cod_livro;"

    consulta = conexao.cursor()
    consulta.execute(codSQL)

    for c in consulta:
        print(c)

    conexao.commit()
    consulta.close()

# 2_5 - Mateus
def show_sold_books_by_id(
    connection
):
    code = int(input('Book code: '))

    codigoSQL =\
        f'''
        SELECT
            cliente.nome AS nome_cliente,
            livro.titulo AS livro_titulo
        FROM
            livro_venda,
            venda,
            cliente,
            livro
        WHERE
            livro_venda.cod_venda = venda.codigo AND
            livro_venda.cod_livro = livro.codigo AND
            venda.cod_cliente = cliente.codigo AND
            livro.codigo = {code}
        GROUP BY nome_cliente
        ORDER BY nome_cliente
        '''
    consulta = connection.cursor()
    consulta.execute(codigoSQL)

    print('--------- CLIENTS ---------')
    for counter, (client, book) in enumerate(consulta):
        if counter == 0:
            print(f'Book: {book}', end='\n\n')
        print(f'{client:<70}')
    print()
    
    consulta.close()

# 2_6 - Mateus
def show_sections(
    connection
):

    codigoSQL =\
        f'''
        SELECT 
            secao.nome AS secao_nome,
            avg(livro_venda.estrelas_avaliacao) AS stars
        FROM
            secao,
            livro_venda,
            livro
        WHERE
            secao.codigo = livro.cod_secao AND
            livro.codigo = livro_venda.cod_livro
        GROUP BY secao_nome
        ORDER BY stars DESC;
        '''
    consulta = connection.cursor()
    consulta.execute(codigoSQL)

    print(f'{"Section":<25} {"Stars":}')
    print('--------- SEÇÕES ---------')
    for section, n_stars in consulta:
        print(f'{section:<25} {n_stars:.2f} {"✬ "*round(int(n_stars))}')
    print()
    
    consulta.close()