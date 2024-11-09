import psycopg2
from questao01 import criar_conexao

def listar_jogos():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        consulta = """SELECT titulo, subtitulo FROM jogos WHERE titulo LIKE '%k%' OR subtitulo LIKE '%k' ORDER BY titulo ASC;"""
        cursor.execute(consulta)
        lista_jogos = cursor.fetchall()

        if lista_jogos:
            for titulo, subtitulo in lista_jogos:
                print(f'Título: {titulo}, Subtítulo: {subtitulo}')
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        cursor.close()
        conn.close()


listar_jogos()