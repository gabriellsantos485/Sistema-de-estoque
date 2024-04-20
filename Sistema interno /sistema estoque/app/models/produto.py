import sqlite3
import sys 
sys.path.append('/home/gabriel/Sistema interno /sistema estoque/app/database')
from conn import cursor
from conn import conexao

conexao = sqlite3.connect('banco_mercado.db')
cursor = conexao.cursor()

class Produto():
    def __init__(self) :
       pass
        
    def inserir_produto(self, nome, descricao, preco_compra, preco_mercado, qtde):
        cursor.execute( """
                       INSERT INTO produtos (nome, descricao, preco_compra, preco_mercado, quantidade) VALUES ( ?, ?, ?, ?, ?)
                       """, (nome, descricao, preco_compra, preco_mercado, qtde)
                       )
        conexao.commit()
        conexao.close()
        cursor.close
        
    def remover_produto(self, id):
        cursor.execute("""
                        DELETE FROM produtos WHERE  id = ?
                       """,  (id)
                       )
        conexao.commit()
        conexao.close()
        cursor.close
    
    def consultar_produtos(self):
        cursor.execute("""
                       SELECT nome FROM produtos 
                       """)
        produtos=cursor.fetchall()
        for nome in produtos:
            print(nome)

    def encontrar_produto(self, produto):
        cursor.execute("SELECT * FROM produtos")
        produto_espec=cursor.fetchall()
        print(produto_espec)
       
        if produto in produto_espec:
            for dado in produto_espec:
                print(produto_espec[dado])
        else:
            print("Produto não encontrado")
    



