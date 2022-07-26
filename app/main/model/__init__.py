from main import ROOT_PATH

def connector():
    from mysql.connector import connect
    import os
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=f'{ROOT_PATH}/.env')

    endereco_ip_sgbd: str = os.getenv('dbms_ip_address')
    nome_esquema: str = os.getenv('schema_name')
    db_user: str = os.getenv('user_dbms')
    senha_usuario_sgbd: str = os.getenv('password_dbms')
    dp_port: str = os.getenv('port')

    return connect(
        host=endereco_ip_sgbd, 
        user=db_user, 
        database=nome_esquema, 
        password=senha_usuario_sgbd,
        port=dp_port
    )