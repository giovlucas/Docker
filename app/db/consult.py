import mysql.connector

# Configurações de conexão ao banco de dados MySQL
config = {
    'host': 'localhost',
    'user': 'test_user',
    'password': 'test_password',
    'database': 'test_db'
}

# Conectar ao banco de dados
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Executar uma consulta de exemplo
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Exibir os resultados
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")

finally:
    # Fechar conexões
    if 'conn' in locals():
        cursor.close()
        conn.close()
