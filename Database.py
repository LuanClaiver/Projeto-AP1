import sqlite3
import sqlite3 as sql

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableCliente()
        self.createTableProduto()

# CRIANDO TABELA CLIENTE
    def createTableCliente(self):
        iniciar = self.conexao.cursor()
        iniciar.execute("""CREATE TABLE IF NOT EXISTS cliente (
                            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome text,
                            email text,
                            endereco text,
                            bairro text,
                            cidade text,
                            telefone integer,
                            sexo text
                            )""")
        self.conexao.commit() # Escrever no arquivo do Banco de dados
        iniciar.close

# CRIANDO TABELA PRODUTO
    def createTableProduto(self):
        iniciar = self.conexao.cursor()
        iniciar.execute("""CREATE TABLE IF NOT EXISTS produto(
                            id_produto INTEGER PRIMARY KEY autoincrement,
                            produto TEXT,
                            marca TEXT,
                            preco FLOAT,
                            quantidade INTEGER,
                            fornecedor TEXT)""")
        self.conexao.commit() # Executar o comando escrevendo no arquivo do Banco de dados
        iniciar.close() # Fechar

# Inserindo Cliente no banco de dados
    def insertCliente(self, nome, email, endereco, bairro, cidade, telefone, sexo):
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("INSERT INTO cliente ( nome, email, endereco, bairro, cidade, telefone, sexo)"
                    "values ('" + nome + "','"
                             '' + email + "','"
                             '' + endereco + "','"
                             '' + bairro + "','"
                             '' + cidade + "','"
                             '' + telefone + "','"
                             '' + sexo + "' "
                             " )") # Consulta
            self.conexao.commit() # Escrever no arquivo do Banco de dados
            iniciar.close()
            return "Cliente cadastrado com sucesso!"
        except:
            return "Erro ao inserir"
    
# Inserindo produto no banco de dados
    def insertProduto(self, produto, marca, preco, quantidade, fornecedor):
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("INSERT INTO produto(produto, marca, preco, quantidade, fornecedor)"
                    "values ('" + produto + "','"
                             '' + marca + "','"
                             '' + preco + "','"
                             '' + quantidade + "','"
                             '' + fornecedor + "' "                         
                             " )") # Consulta
            self.conexao.commit() # Escrever no arquivo do Banco de dados
            iniciar.close()
            return "Produto cadastrado com sucesso!"
        except:
            return "Erro ao inserir"

# DELETANDO CLIENTE
    def deleteCliente(self, id_cliente):
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("DELETE FROM cliente WHERE id_cliente = ?", (id_cliente,))
            self.conexao.commit() # Escrever no arquivo do Banco de dados
            iniciar.close()
            return "Cliente excluido com sucesso"
        except:
            return "Falha ao excluir"

# DELETANDO PRODUTO
    def deleteProduto(self, id_produto):
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("DELETE FROM produto WHERE id_produto = ?", (id_produto,))
            self.conexao.commit() # Escrever no arquivo do Banco de dados
            iniciar.close()
            return "Produto excluido com sucesso"
        except:
            return "Falha ao excluir"

# Select cliente tabela
    def selectClienteTabela(self):
        # Lista vazia
        tabela = []
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("SELECT * FROM cliente")
            for linha in iniciar: # Percorendo linhas da lista
                cliente = []
                cliente.append(linha[0])
                cliente.append(linha[1])
                cliente.append(linha[2])
                cliente.append(linha[3])
                cliente.append(linha[4])
                cliente.append(linha[5])
                cliente.append(linha[6])
                cliente.append(linha[7])
                tabela.append(cliente)
            iniciar.close()
            return tabela
        except:
            return "Falha ao buscar"

# Selecionando Produto
    def selectProdutoTabela(self):
        # Lista vazia
        tabela = []
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("SELECT * FROM produto")
            for linha in iniciar: # Percorendo linhas da lista
                produto = []
                produto.append(linha[0])
                produto.append(linha[1])
                produto.append(linha[2])
                produto.append(linha[3])
                produto.append(linha[4])
                produto.append(linha[5])
                tabela.append(produto)
            iniciar.close()
            return tabela
        except:
            return "Falha ao buscar"
        
######## Parte de realizar compra #######
    def selectProdutoCompra(self, produto):
        # Lista vazia
        tabela = []
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("SELECT * FROM produto LIKE %?% ", (produto,))
            for linha in iniciar: # Percorendo linhas da lista
                produto = []
                produto.append(linha[1])
                produto.append(linha[3])
                tabela.append(produto)
            iniciar.close()
            print(tabela)
            return tabela
        except:
            return "Falha ao buscar Produto"    
    
    # Atualizando Cliente
    def updateCliente(self, nome, email, endereco, bairro, cidade, telefone, sexo, id_cliente):
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("UPDATE cliente SET nome = '" + nome + "', email = '" + email + "', endereco = '" + endereco + "', bairro = '" + bairro + "', cidade = '" + cidade + "', telefone = '" + telefone + "', sexo = '" + sexo + "' WHERE id_cliente = '" + id_cliente + "' ")
            self.conexao.commit()
            iniciar.close()
            return "Cliente atualizado"
        except:
            return "Error update"
    
    # Atualizando Produto
    def updateProduto(self, produto, marca, preco, quantidade, fornecedor, id_produto):
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("UPDATE produto SET produto = '" + produto + "', marca = '" + marca + "', preco = '" + preco + "', quantidade = '" + quantidade + "', fornecedor = '" + fornecedor + "' WHERE id_produto = '" + id_produto + "' ")
            self.conexao.commit()
            iniciar.close()
            return "Produto Atualizado"            
        except:
            return "Error update"

    # Mostrar Produtos na compra
    def mostrarProdutos(produto, preco):
        tabela = []
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("SELECT produto, preco FROM produto")
            for linha in iniciar: # Percorendo linhas da lista
                produto = []
                produto.append(linha[0])
                produto.append(linha[2])    
                tabela.append(produto)            
            iniciar.close()
            return tabela
        except:
            return "Erro ao mostrar"

    # Buscar Produtos na compra
    def buscarProdutos():
        tabela = []
        try:
            iniciar = self.conexao.cursor()
            iniciar.execute("SELECT produto FROM produto")
            for linha in iniciar: # Percorrendo linhas da lista
                produto = []
                produto.append(linha[0])
                tabela.append(produto)
            iniciar.close()
            return tabela
        except:
            return "Falha ao buscar"
