import pytest
from utils.database import Database

def test_conexao_database():
    conn = Database.conectar()
    assert conn is not None, "A conexão com o banco de dados falhou."
    assert conn.is_connected(), "A conexão não está ativa."
    conn.close()

def test_sql_select():
    # Testa um comando SQL simples
    conn = Database.conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result[0] == 1, "O SELECT 1 não retornou o valor esperado."
    cursor.close()
    conn.close()

def test_sql_insert():
    # Exemplo de insert fictício, ajuste para sua tabela real
    sql = "INSERT INTO test_table (name) VALUES (%s)"
    dados = ("Teste",)
    rowcount = Database.executar_sql(sql, dados)
    assert rowcount == 1 or rowcount is not None, "O insert não foi realizado."
