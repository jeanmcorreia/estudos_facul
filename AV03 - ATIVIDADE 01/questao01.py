import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname='postgre',
            user='postgres',
            password='post',
            host='localhost',
            port='5432'
        )
        return conn
    except Exception as e:
        print("Erro ao conectar com o banco de dadoos: {e}")
        return None
    
def listar_jogos():
    conn = criar_conexao()
    try:
        nome = input('Digite o nome do jogo: ')
        cursor = conn.cursor()
        consulta = "SELECT titulo FROM aula.jogos WHERE titulo ILIKE %s"
        cursor.execute(consulta, (f"%{nome}%",))
        resultado = cursor.fetchall()
        conn.commit()
        for linha in resultado:
            print(resultado)
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        cursor.close()
        conn.close()


listar_jogos()
