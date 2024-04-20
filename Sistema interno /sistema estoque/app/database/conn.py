import sqlite3

# Conectar ao banco de dados (se não existir, será criado automaticamente)
conexao = sqlite3.connect('banco_mercado.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar uma tabela chamada 'produtos' (se ainda não existir IF NOT etc; )
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    preco_compra FLOAT NOT NULL,
                    preco_mercado  FLOAT NOT NULL,
                    quantidade INTEGER
                  )''')


# Commitar as alterações e fechar a conexão
conexao.commit()
conexao.close()