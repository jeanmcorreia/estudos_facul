import psycopg2
from questao01 import criar_conexao

def listar_titulos():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo FROM aula.jogos WHERE id > 0;")
        resultado = cursor.fetchall()
        for linha in resultado:
            print(f'Título: {linha[1]} - id: {linha[0]}')
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        cursor.close()
        conn.close()

listar_titulos()
    