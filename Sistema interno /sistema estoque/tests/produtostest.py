import sys
sys.path.append('/home/gabriel/Sistema interno /sistema estoque/app/models')
from produto import Produto

produtos_loja = Produto()
produtos_loja.inserir_produto(nome="Sabonete Albon", descricao="Melhor sabonete", preco_compra=2, preco_mercado=3, qtde=50)
#produtos_loja.remover_produto(id="3")
#produtos_loja.consultar_produtos()
#produtos_loja.encontrar_produto("Abobóra")