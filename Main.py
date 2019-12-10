# Algoritmos e Programação 1
# Professor: Dr. Yuri Lacerda
# Equipe: Luan Claiver
#         Antonia Priscila
#         Jose Alci
#         Pedro Igor

#Importar os modulos Necessarios
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Database import Banco

# ----------------------- Funções ------------------------
def sair():
    janela.destroy()

def verClientesCadastrados():
    #------- Cria uma janela secundaria que exibe o que foi salvo -------
    janelaView = Tk()
    janelaView.resizable(0,0)
    janelaView.title("Dados inseridos")

    # Forma de vizualização do arquivo com os dados
    txtView = Text(janelaView, fg = "red", bg = "white")
    txtView.pack()
    # Abre o arquivo txt, caso nao exista ele é criado
    arquivo = open("CLIENTESCADASTRADOS.txt")
    lista   = arquivo.readlines()

    # Percorre a lista para mostrar os dados que foram salvos
    for dados in range(len(lista)):
        j = lista[dados]
        txtView.insert(END, j + "\n")

    arquivo.close()
    janelaView.mainloop()

def verProdutosCadastrados():
    #------- Cria uma janela secundaria que exibe o que foi salvo -------
    janelaView = Tk()
    janelaView.resizable(0,0)
    janelaView.title("Dados inseridos")

    # Forma de vizualização do arquivo com os dados
    txtView = Text(janelaView, fg = "red", bg = "white")
    txtView.pack()
    # Abre o arquivo txt, caso nao exista ele é criado
    arquivo = open("PRODUTOSCADASTRADOS.txt")
    lista = arquivo.readlines()

    # Percorre a lista para mostrar os dados que foram salvos
    for dados in range(len(lista)):
        j = lista[dados]
        txtView.insert(END, j + "\n")

    arquivo.close()
    janelaView.mainloop()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#               Funcao de Cadastro de clientes
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def CadastrandoCliente():
    janela = Tk()
    janela.geometry("500x500+500+0")
    janela["bg"] = "#9ACD32"
    janela.title("Cadastro de clientes")

    #   FRAME DE CIMA
    framef0 = Frame(janela, background = "#03A9F4", width = 500, height = 100, bd = 8, relief = "raise")
    framef0.place(x= 0, y = 0)

    # Mensagem de Inicio
    mensagem1 = Label(janela, text = 'Cadastrando Cliente', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
    mensagem1.place(x = 110, y = 30)
    # FRAME DE BAIXO
    framef1 = Frame(janela, width = 500, height = 400, bd = 8, relief = "raise")
    framef1.place(x= 0, y = 100)

    # CRIANDO VARIAVEIS PARA ARMAZENAR O TEXTO INSERIDO PELO USUARIO
    txtNome      = StringVar()
    txtEmail     = StringVar()
    txtEndereco  = StringVar()
    txtTelefone  = StringVar()
    txtBairro    = StringVar()
    
    # CRIANDO OS OBJETOS QUE ESTARAO NA JANELA
    labelNome       = Label(janela, text = "Nome:", font = ("bold", 10))
    labelEmail      = Label(janela, text = "Email:", font = ("bold", 10))
    labelEndereco   = Label(janela, text = "Endereco:", font = ("bold", 10))
    labelBairro     = Label(janela, text = "Bairro:", font = ("bold", 10))
    labelTelefone   = Label(janela, text = "Telefone:", font = ("bold", 10))
    labelSexo       = Label(janela, text = "Sexo:", font = ("bold", 10))
    labelCidade     = Label(janela, text = "Cidade:", font = ("bold", 10))

    entryNome       = Entry(janela, width = 50, textvariable = txtNome)
    entryEmail      = Entry(janela, width = 50, textvariable = txtEmail)
    entryEndereco   = Entry(janela, width = 50, textvariable = txtEndereco)
    entryBairro     = Entry(janela, width = 50, textvariable = txtBairro)
    entryTelefone   = Entry(janela, width = 50, textvariable = txtTelefone)
    
    # UTILIZEI O METODO PLACE DO TKINTER PARA POSICIONAR OS OBJETOS NA JANELA
    labelNome.place(x = 10, y = 120)
    labelEmail.place(x = 10, y = 150)
    labelEndereco.place(x = 10, y = 180)
    labelBairro.place(x = 10, y = 210)
    labelCidade.place(x = 10, y = 300)
    labelTelefone.place(x = 10, y = 240)
    labelSexo.place(x = 10, y = 270)

    entryNome.place(x = 80, y = 120)
    entryEmail.place(x = 80, y = 150)
    entryEndereco.place(x = 80, y = 180)
    entryBairro.place(x = 80, y = 210)
    entryTelefone.place(x = 80, y = 240)

    labelSexo = Label(janela, text = "Sexo:", font = ("bold", 10))
    listSexo = ['Masculino', 'Feminino', 'Outros']
    s = StringVar(janela)
    s.set("Não Informado")
    dropListSexo = OptionMenu(janela, s, *listSexo)
    dropListSexo.config(width = 15, font = ("bold", 10))
    dropListSexo['bg'] = "#03A9F4"
    dropListSexo.place(x = 120, y = 270)

    labelCidade = Label(janela, text = "Cidade do cliente:", font = ("bold", 10))
    listaCidades = ['Araripe', 'Barbalha', 'Crato', 'Jardim', 'Juazeiro', 'Nova Olinda']
    #  C INICIA A STRING COM UM VALOR PREDEFINIDO
    c = StringVar(janela) # Necessario passar o parametro
    c.set ("- Selecione -")
    dropList = OptionMenu(janela, c, *listaCidades)
    dropList.config(width = 15, font = ("bold", 10))
    dropList['bg']= "#03A9F4"
    dropList.place(x = 120, y = 300)

    # Salvando no Banco
    def salvar():
        banco = Banco()
        
        nome     = str(entryNome.get())
        endereco = str(entryEndereco.get())
        bairro   = str(entryBairro.get())
        telefone = str(entryTelefone.get())
        email    = str(entryEmail.get())
        sexo     = str(s.get())
        cidade   = str(c.get())

        if(c.get() == "Selecione"):
            cidade = "Nao Informado"
        # Verifica se caixas de texto foram preenchidas, se nao foram, apresenta erro, se foram salva no arquivo
        if(nome == ""):
            messagebox.showerror("Error", "Favor preencher o nome do CLIENTE")
        elif(endereco == ""):
            endereco == "Não informado"
        elif(bairro == ""):
            messagebox.showerror("Error", "Favor preencher o campo BAIRRO")
        elif(telefone == ""):
            messagebox.showerror("Error", "Favor preencher o campo TELEFONE")
        elif(email == ""):
            messagebox.showerror("Error", "Favor preencher o campo EMAIL")
        else:
            banco.insertCliente(nome, email, endereco, bairro, cidade, telefone, sexo)

            # Escreve no arquivo.txt as informações do cliente
            arquivo = open("CLIENTESCADASTRADOS.txt", "a")
            arquivo.write("@@@@@@@@@@@@@@@   Cadastro de Cliente   @@@@@@@@@@@@@" + "\n")
            arquivo.write("-----------------------------------------------------")
            arquivo.writelines("\n" + "Nome:" + nome + "\n" + "E-mail:" + email + "\n" + "Endereco:" + endereco + "\n" + "Bairro:" + bairro + "\n" +
            "Telefone:" + telefone + "\n" + "Sexo:" + sexo + "\n" + "Cidade:" + cidade + "\n")
            arquivo.write("-----------------------------------------------------" + "\n")
            arquivo.close()

            messagebox.showinfo("Info", "Salvo com sucesso!")
            janela.destroy()

    # COLOCANDO BOTOES NA TELA
    botaoSalvar                 = Button(janela, width = 16, height = 6, text = "Salvar", bg = "#00c853", command = salvar) # Botao Verde
    botaoVerClientesCadastrados = Button(janela, width = 16, height = 6, text = "Listar", bg="#03A9F4", command = verClientesCadastrados) # Botao Azul
    botaoSair                   = Button(janela, width = 16, height = 6, bg = "#c62828", text = "Sair", command = janela.destroy) # Botao Vermelho

    botaoSalvar.place(x = 40, y= 350) # Botao Verde 
    botaoVerClientesCadastrados.place(x=190, y=350) # Botao Azul   
    botaoSair.place(x = 340, y = 350) # Botao Vermelho

    janela.mainloop() # Mantem a janela em execução

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#           Funcao Cadastro de Produtos
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def CadastrandoProduto(): # Funcao cadastrando Produto
    janela = Tk()
    janela.geometry("500x500+0+0")
    janela["bg"] = "#9ACD32"
    janela.title("Cadastro de Produtos")

    def salvar():  # FUNCAO PARA SALVAR NO BANCO DE DADOS E SALVAR NO ARQUIVO DE TXT
        banco = Banco()

        produto    = str(entryProduto.get())
        marca      = str(entryMarca.get())
        preco      = str(entryPreco.get())
        quantidade = str(entryQuantidade.get())
        fornecedor = str(entryFornecedor.get())
    
        # Verifica se caixas de texto foram preenchidas, se nao foram, apresenta erro, se foram salva no arquivo
        if(produto == ""):
            messagebox.showerror("Error", "Favor preencher o nome do PRODUTO")
        if(quantidade == ""):
            quantidade == "Não informado"
        if(marca == ""):
            marca == "Não informado"
        elif(preco == ""):
            messagebox.showerror("Error", "Favor preencher o campo PRECO")
        elif(fornecedor == ""):
            fornecedor == "Não informado"
        else:
            banco.insertProduto(produto, marca, preco, quantidade, fornecedor)

            # Escreve no arquivo.txt as informações do produto
            arquivo = open("PRODUTOSCADASTRADOS.txt", "a")
            arquivo.write("@@@@@@@@@@@@@@@   Cadastro de Produto   @@@@@@@@@@@@@" + "\n")
            arquivo.write("-----------------------------------------------------")
            arquivo.writelines("\n" + "Produto:" + produto + "\n" + "Marca:" + marca + "\n" + "preco:" + preco + "\n" +
            "Quantidade:" + quantidade + "\n" + "Fornecedor:" + fornecedor + "\n")
            arquivo.write("-----------------------------------------------------" + "\n")
            arquivo.close()

            messagebox.showinfo("Info", "Salvo com sucesso!")

        janela.destroy()

    # FRAME DE CIMA
    framef0 = Frame(janela, background = "#03A9F4", width = 500, height = 100, bd = 8, relief = "raise")
    framef0.place(x = 0, y = 0)

    # Mensagem de Inicio
    mensagem1 = Label(janela, text = 'Cadastrando Produto', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
    mensagem1.place(x = 110, y = 30)
    # FRAME DE BAIXO
    framef1 = Frame(janela, width = 500, height = 400, bd = 8, relief = "raise")
    framef1.place(x = 0, y = 100)

    labelProduto = Label(janela, text = "Produto:", font = ("bold", 10))
    labelProduto.place(x = 10, y = 120)
    entryProduto = Entry(janela, width = 30)
    entryProduto.place(x = 80, y = 120)

    labelMarca = Label(janela, text = "Marca:", font = ("bold", 10))
    labelMarca.place(x = 10, y = 150)
    entryMarca = Entry(janela, width = 30)
    entryMarca.place(x = 80, y = 150)

    labelPreco = Label(janela, text = "Preco:", font = ("bold", 10))
    labelPreco.place(x = 10, y = 180)
    entryPreco = Entry(janela, width = 30)
    entryPreco.place(x = 80, y = 180)

    labelQuantidade = Label(janela, text = "Quantidade:", font = ("bold", 10))
    labelQuantidade.place(x = 10, y = 210)
    entryQuantidade = Entry(janela, width = 30)
    entryQuantidade.place(x = 80, y = 210)

    labelFornecedor = Label(janela, text = "Fornecedor:", font = ("bold", 10))
    labelFornecedor.place(x = 10, y = 240)
    entryFornecedor = Entry(janela, width = 30)
    entryFornecedor.place(x = 80, y = 240)
   # BOTOES GRANDES - VERDE/ AZUL E VERMELHO
    botaoSalvar = Button(janela, width = 16, height = 6, text = "Salvar", bg = "#00c853", command = salvar)
    botaoSalvar.place(x = 40, y= 350) # Pequenos -> x = 20, y = 400

    botaoVerClientesCadastrados = Button(janela, width = 16, height = 6, text = "Listar", bg="#03A9F4", command=verProdutosCadastrados)
    botaoVerClientesCadastrados.place(x=190, y=350)# Pequenos -> x = 170, y = 400

    botaoSair = Button(janela, width = 16, height = 6, bg = "#c62828", text = "Sair", command = janela.destroy)
    botaoSair.place(x = 340, y = 350) # Pequenos -> x = 320, y = 400
    janela.mainloop()

##################################################################################################################################################################
#     ###### REGISTRANDO COMPRA DE CLIENTE #######
# def registraCompra():
#     janela = Tk()
#     janela.geometry("500x600+0+0")
#     # janela.resizable(0, 0)
#     janela["bg"] = "#9ACD32"
#     janela.title("Registro de compra")

#     # FRAME DE CIMA
#     framef0 = Frame(janela, background = "#03A9F4", width = 500, height = 100, bd = 8, relief = "raise")
#     framef0.place(x = 0, y = 0)

#     # Mensagem de Inicio
#     mensagem1 = Label(janela, text = 'Registrando compra', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
#     mensagem1.place(x = 110, y = 30)
#     # FRAME DE BAIXO
#     framef1 = Frame(janela, width = 500, height = 500, bd = 8, relief = "raise")
#     framef1.place(x = 0, y = 100)

#     # Widgets
#     frame2 = Frame(janela).pack(side = TOP, fill = BOTH, padx = 5, pady = 5)
#     frame4 = Frame(janela).pack(side = BOTTOM, padx = 5)
 
#     def finalizarCompra():
#         pass

#     def mostrarProdutos():
#         pass

#     txtProd = StringVar()

#     #Labels
#     lblProduto         = Label(janela, text = "Produto:", font = ("Arial", 10)).place(x = 12, y = 110)
#     label2             = Label(janela, text = "Total de produtos", font = ("Arial", 10)).place(x = 12, y = 240)
#     labelTotalDinheiro = Label(janela, text = "Total R$ = ", font = ("Arial", 20)).place(x = 250, y = 300)
#     labelDinheiro      = Label(janela, text = "0,00", font = ("Arial", 20)).place(x = 390, y = 300)
#     entrylblProduto    = Entry(janela, width = 25, textvariable = txtProd).place(x = 80, y = 115)

#     # scrollProduto      = Scrollbar(janela, orient = VERTICAL)
#     listaProduto       = Listbox(janela, width = 75, height = 5) # , yscrollcommand = scrollProduto.set
#     # scrollProduto.config(command = listaProduto.yview)
#     # scrollProduto.pack(side = RIGHT, fill = Y)
#     listaProduto.place(x = 12, y = 150)

#     listTotal          = Listbox(janela, width = 25, height = 15).place(x = 12, y = 280)

#     # entrada = str(txtProd.get())

#     def buscar():
#         banco = Banco()
#         # selected_produto = listProdutos.curselection()[0] # Atribuindo o clique a variavel
#         # new_lista        = banco.selectProdutoTabela() # Selecionando todos os produtos no banco
#         # new_produto      = new_lista[selected_produto] # Atribuindo o produto que foi clicado 
#         lista = banco.selectProdutoCompra(str(txtProd.get()))
#         for i in range(len(lista)):
#             listaProduto.insert(END, lista[i])

#     # BOTOES
#     botaoBuscar          = Button(janela, width = 20, text = "Buscar", font = ("Arial", 10), command = buscar).place(x = 250, y = 110)
#     botaoFinalizarCompra = Button(janela, text = "Finalizar Compra", font = ("Arial", 10), command = finalizarCompra).place(x = 75, y = 540)
#     botaoVerProdutos     = Button(janela, text = "Mostrar", font = ("Arial", 10), command = mostrarProdutos).place(x = 12, y = 540)
#     botaoSair            = Button(janela, width = 16, height = 6, bg = "#c62828", text = "Sair", command = janela.destroy).place(x = 360, y = 480)

##################################################################################################################################################################
def verProdutos():
    janela = Tk()
    janela.geometry("500x600+0+0")
    janela["bg"] = "#9ACD32"
    janela.title("Produtos")

    # FRAME DE CIMA
    framef0 = Frame(janela, background = "#03A9F4", width = 485, height = 100, bd = 8, relief = "raise")
    framef0.place(x = 0, y = 0)

    # Mensagem de Inicio
    mensagem1 = Label(janela, text = 'Produtos cadastrados', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
    mensagem1.place(x = 110, y = 30)
    # FRAME DE BAIXO
    framef1 = Frame(janela, width = 485, height = 500, bd = 8, relief = "raise")
    framef1.place(x = 0, y = 100)

    banco = Banco()

    # Criando objetos que estarão na tela e ligando um objeto ao outro
    scrollProdutos = Scrollbar(janela, orient = VERTICAL)
    listProdutos = Listbox(janela, width = 75, height = 20, yscrollcommand = scrollProdutos.set) # opção de comando que são chamados quando forem necessarias para a barra de rolagem para ser atualizado
    scrollProdutos.config(command = listProdutos.yview)
    scrollProdutos.pack(side = RIGHT, fill = Y)
    listProdutos.place(x = 12, y = 110)

    def atualizar():
        janela = Tk()
        janela.geometry("500x500+0+0")
        janela["bg"] = "#9ACD32"
        janela.title("Atualizacao de Produtos")

        banco = Banco()
        selected_produto = listProdutos.curselection()[0] # Atribuindo o clique a variavel
        new_lista        = banco.selectProdutoTabela() # Selecionando todos os produtos no banco
        new_produto      = new_lista[selected_produto] # Atribuindo o produto que foi clicado 

        # FRAME DE CIMA
        framef0 = Frame(janela, background = "#03A9F4", width = 500, height = 100, bd = 8, relief = "raise")
        framef0.place(x = 0, y = 0)

        # Mensagem de Inicio
        mensagem1 = Label(janela, text = 'Atualizando Produto', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
        mensagem1.place(x = 110, y = 30)
        # FRAME DE BAIXO
        framef1 = Frame(janela, width = 500, height = 400, bd = 8, relief = "raise")
        framef1.place(x = 0, y = 100)

        # CRIANDO VARIAVEIS PARA ARMAZENAR O TEXTO INSERIDO PELO USUARIO
        txtProduto     = StringVar()
        txtMarca       = StringVar()
        txtPreco       = StringVar()
        txtQuantidade  = StringVar()
        txtFornecedor  = StringVar()

        # CRIANDO OBJETOS QUE ESTARAO NA TELA
        labelProduto     = Label(janela, text = "Produto:", font = ("bold", 10))
        labelMarca       = Label(janela, text = "Marca:", font = ("bold", 10))
        labelPreco       = Label(janela, text = "Preco:", font = ("bold", 10))
        labelQuantidade  = Label(janela, text = "Quantidade:", font = ("bold", 10))
        labelFornecedor  = Label(janela, text = "Fornecedor:", font = ("bold", 10))

        entryProduto     = Entry(janela, width = 30)
        entryMarca       = Entry(janela, width = 30)
        entryPreco       = Entry(janela, width = 30)        
        entryQuantidade  = Entry(janela, width = 30)
        entryFornecedor  = Entry(janela, width = 30)

        # UTILIZANDO O METODO PLACE PARA POSICIONAR OS OBJETOS NA JANELA
        labelProduto.place(x = 10, y = 120)
        labelMarca.place(x = 10, y = 150)
        labelPreco.place(x = 10, y = 180)
        labelQuantidade.place(x = 10, y = 210)
        labelFornecedor.place(x = 10, y = 240)

        entryProduto.place(x = 80, y = 120)
        entryMarca.place(x = 80, y = 150)
        entryPreco.place(x = 80, y = 180)
        entryQuantidade.place(x = 80, y = 210)
        entryFornecedor.place(x = 80, y = 240)

        # INSERINDO VALORES AS LINHAS PARA SEREM MODIFICADOS
        entryProduto.insert(0, new_produto[1])
        entryMarca.insert(0, new_produto[2])
        entryPreco.insert(0, new_produto[3])
        entryQuantidade.insert(0, new_produto[4])
        entryFornecedor.insert(0, new_produto[5])

        def atualizarProduto():            
            id_produto = str(new_produto[0])
            produto    = str(entryProduto.get())
            marca      = str(entryMarca.get())
            preco      = str(entryPreco.get())
            quantidade = str(entryQuantidade.get())
            fornecedor = str(entryFornecedor.get())

            banco = Banco()
            banco.updateProduto(produto, marca, preco, quantidade, fornecedor, id_produto)
            messagebox.showinfo("Info", "Atualizado com sucesso!")

        # Botoes
        botaoAtualizar = Button(janela, text = "Salvar", width = 16, height = 6, bg = "#00c853", command = atualizarProduto).place(x = 90, y = 360)
        botaoSair      = Button(janela, text = "Sair", width = 16, height = 6, bg = "#c62828", command = janela.destroy).place(x = 260, y = 360)
        
        janela.mainloop()
           
    # Lista todos os produtos cadastrados, percorrendo os arquivos no SQLite3
    lista = banco.selectProdutoTabela()
    for i in range(len(lista)):
        listProdutos.insert(END, lista[i])

    def deletar():
        banco = Banco()
        selected_produto = listProdutos.curselection()[0] # Atribuindo o produto selecionado a variavel
        new_lista = banco.selectProdutoTabela() # Selecionando todos os produtos do banco.
        new_produto = new_lista[selected_produto] # Atribuindo o cliente que foi clicado.
        banco.deleteProduto(new_produto[0]) # Deletando o produto a partir do ID que foi passado como parametro.
        listProdutos.delete(selected_produto, END) # Remove o produto da Listbox.

    # botaoVerTodos  = Button(janela, text = "Ver todos", width = 20, command = verTodos).place(x = 330, y = 350)
    botaoDeletar   = Button(janela, text = "Deletar  ", width = 16, height = 6, bg = "#00c853", command = deletar).place(x = 50, y = 460)
    botaoAtualizar = Button(janela, text = "Editar Produto", width = 16, height = 6, bg="#03A9F4", command = atualizar).place(x = 180, y = 460)
    botaoSair      = Button(janela, text = "Sair"     , width = 16, height = 6, bg = "#c62828", command = janela.destroy).place(x = 310, y = 460)

def verClientes():
    janela = Tk()
    janela.geometry("500x600+0+0")
    janela["bg"] = "#9ACD32"
    janela.title("Clientes Fixos")
    
    # FRAME DE CIMA
    framef0 = Frame(janela, background = "#03A9F4", width = 485, height = 100, bd = 8, relief = "raise")
    framef0.place(x = 0, y = 0)

    # Mensagem de Inicio
    mensagem1 = Label(janela, text = 'Clientes cadastrados', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
    mensagem1.place(x = 110, y = 30)
    # FRAME DE BAIXO
    framef1 = Frame(janela, width = 485, height = 500, bd = 8, relief = "raise")
    framef1.place(x = 0, y = 100)

    banco = Banco()

    # Criando objetos que estarão na tela
    scrollClientes = Scrollbar(janela, orient = VERTICAL)
    listClientes = Listbox(janela, width = 75, height = 20, yscrollcommand = scrollClientes.set)
    scrollClientes.config(command = listClientes.yview)
    scrollClientes.pack(side = RIGHT, fill = Y)
    listClientes.place(x = 12, y = 110)

    def atualizar():
        janela = Tk()
        janela.geometry("500x500+500+0")
        janela["bg"] = "#9ACD32"
        janela.title("Atualização de cliente")

        banco = Banco()
        selected_cliente = listClientes.curselection()[0] # Atribuindo o cliente selecionado a variavel
        new_lista = banco.selectClienteTabela() # Selecionando todos os clientes do banco.
        new_cliente = new_lista[selected_cliente] # Atribuindo o cliente que foi clicado.

        #   FRAME DE CIMA
        framef0 = Frame(janela, background = "#03A9F4", width = 500, height = 100, bd = 8, relief = "raise")
        framef0.place(x= 0, y = 0)

        # Mensagem de Inicio
        mensagem1 = Label(janela, text = 'Atualização de Cliente', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
        mensagem1.place(x = 110, y = 30)
        # FRAME DE BAIXO
        framef1 = Frame(janela, width = 500, height = 400, bd = 8, relief = "raise")
        framef1.place(x= 0, y = 100)

        # CRIANDO VARIAVEIS PARA ARMAZENAR O TEXTO INSERIDO PELO USUARIO
        txtNome      = StringVar()
        txtEmail     = StringVar()
        txtEndereco  = StringVar()
        txtTelefone  = StringVar()
        txtBairro    = StringVar()
        
        # CRIANDO OS OBJETOS QUE ESTARAO NA JANELA
        labelId         = Label(janela, text = "ID", font = ("bold", 10))
        labelIdValor    = Label(janela, text = str(new_cliente[0]), font = ("bold", 15))
        labelNome       = Label(janela, text = "Nome:", font = ("bold", 10))
        labelEmail      = Label(janela, text = "Email:", font = ("bold", 10))
        labelEndereco   = Label(janela, text = "Endereco:", font = ("bold", 10))
        labelBairro     = Label(janela, text = "Bairro:", font = ("bold", 10))
        labelTelefone   = Label(janela, text = "Telefone:", font = ("bold", 10))
        labelSexo       = Label(janela, text = "Sexo:", font = ("bold", 10))
        labelCidade     = Label(janela, text = "Cidade:", font = ("bold", 10))

        entryNome       = Entry(janela, width = 50, textvariable = txtNome)
        entryEmail      = Entry(janela, width = 50, textvariable = txtEmail)
        entryEndereco   = Entry(janela, width = 50, textvariable = txtEndereco)
        entryBairro     = Entry(janela, width = 50, textvariable = txtBairro)
        entryTelefone   = Entry(janela, width = 50, textvariable = txtTelefone)
        
        # UTILIZANDO O METODO PLACE PARA POSICIONAR OS OBJETOS NA JANELA
        labelId.place(x = 430, y = 120)
        labelIdValor.place(x = 430, y = 150)
        labelNome.place(x = 10, y = 120)
        labelEmail.place(x = 10, y = 150)
        labelEndereco.place(x = 10, y = 180)
        labelBairro.place(x = 10, y = 210)
        labelCidade.place(x = 10, y = 310)
        labelTelefone.place(x = 10, y = 240)
        labelSexo.place(x = 10, y = 270)

        entryNome.place(x = 80, y = 120)
        entryEmail.place(x = 80, y = 150)
        entryEndereco.place(x = 80, y = 180)
        entryBairro.place(x = 80, y = 210)
        entryTelefone.place(x = 80, y = 240)

        entryNome.insert(0, new_cliente[1])
        entryEmail.insert(0, new_cliente[2])
        entryEndereco.insert(0, new_cliente[3])
        entryBairro.insert(0, new_cliente[4])
        entryTelefone.insert(0, new_cliente[6])

        labelSexo = Label(janela, text = "Sexo:", font = ("bold", 10))
        listSexo = ['Masculino', 'Feminino', 'Outros']
        s = StringVar(janela)
        s.set(new_cliente[7])
        dropListSexo = OptionMenu(janela, s, *listSexo)
        dropListSexo.config(width = 15, font = ("bold", 10), )
        dropListSexo['bg'] = "#03A9F4"
        dropListSexo.place(x = 100, y = 270)

        labelCidade = Label(janela, text = "Cidade do cliente:", font = ("bold", 10))
        listaCidades = ['Araripe', 'Barbalha', 'Crato', 'Jardim', 'Juazeiro', 'Nova Olinda']
        #  C INICIA A STRING COM UM VALOR PREDEFINIDO
        c = StringVar(janela) # Necessario passar o parametro
        c.set(new_cliente[5])
        dropList = OptionMenu(janela, c, *listaCidades)
        dropList.config(width = 15, font = ("bold", 10))
        dropList['bg']= "#03A9F4"
        dropList.place(x = 100, y = 310)

        def atualizarCliente():            
            id_cliente = str(labelIdValor['text'])
            nome       = str(entryNome.get())
            endereco   = str(entryEndereco.get())
            bairro     = str(entryBairro.get())
            telefone   = str(entryTelefone.get())
            email      = str(entryEmail.get())
            sexo       = str(s.get())
            cidade     = str(c.get())

            banco = Banco()
            banco.updateCliente(nome, email, endereco, bairro, cidade, telefone, sexo, id_cliente)
            messagebox.showinfo("Info", "Atualizado com sucesso!")

        # Botoes
        botaoAtualizar = Button(janela, text = "Salvar", width = 16, height = 6, bg = "#00c853", command = atualizarCliente).place(x = 90, y = 360)
        botaoSair      = Button(janela, text = "Sair", width = 16, height = 6, bg = "#c62828", command = janela.destroy).place(x = 260, y = 360)              

    # # Lista todos os clientes cadastrados, percorrendo os arquivos no SQLite3
    lista = banco.selectClienteTabela()
    for i in range(len(lista)):
        listClientes.insert(END, lista[i])
    
    def deletar():
        banco = Banco()
        selected_cliente = listClientes.curselection()[0] # Atribuindo o cliente selecionado a variavel
        new_lista = banco.selectClienteTabela() # Selecionando todos os clientes do banco.
        new_cliente = new_lista[selected_cliente] # Atribuindo o cliente que foi clicado.
        banco.deleteCliente(new_cliente[0]) # Deletando o cliente a partir do ID que foi passado como parametro.
        listClientes.delete(selected_cliente, END) # Remove o cliente da Listbox.

    # botaoVerTodos  = Button(janela, text = "Ver todos", width = 20, command = verTodos).place(x = 330, y = 350)
    botaoDeletar   = Button(janela, text = "Deletar  ", width = 16, height = 6, bg = "#00c853", command = deletar).place(x = 50, y = 460)
    botaoAtualizar = Button(janela, text = "Editar Cliente", width = 16, height = 6, bg="#03A9F4", command = atualizar).place(x = 180, y = 460)
    botaoSair      = Button(janela, text = "Sair"     , width = 16, height = 6, bg = "#c62828", command = janela.destroy).place(x = 310, y = 460)


# ----------------------  JANELA PRINCIPAL ------------------------
janela = Tk()                     # CRIACAO DA GUI
janela.geometry("500x600+0+0")
janela["bg"] = "#4ACD32"
janela.title("SISTEMA MERCADO")

# FRAME DE CIMA
framef0 = Frame(janela, background = "#03A9F4", width = 500, height = 150, bd = 8, relief = "raise")
framef0.place(x= 0, y = 0)
# Mensagens de Inicio
mensagem1 = Label(janela, text = 'Sistema de cadastro 4.0', font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
mensagem1.place(x = 80, y = 70)
mensagem2 = Label(janela, text = "Janela Principal", font = ("arial", 20, "bold"), background = "#03A9F4", foreground = "white")
mensagem2.place(x = 140, y = 20)
# FRAME DE BAIXO
framef1 = Frame(janela, background = "#00c853", width = 500, height = 500, bd = 8, relief = "raise")
framef1.place(x= 0, y = 150)
# ADICIONANDO IMAGEM
imagem = PhotoImage(file = "carrinho.png")
labelImagem = Label(janela, image = imagem).place(x = 0, y = 150)

# ADICIONANDO BOTOES PRINCIPAIS
botaoCadastrarCliente           = Button(janela, width = 60, height = 3, text = "Cadastrar Cliente" , bg = "#fafafa", command = CadastrandoCliente) # Botao que abre outra janela com labels para cadastro de clientes
botaoCadastrarProduto           = Button(janela, width = 60, height = 3, text = "Cadastrar Produto" , bg = "#fafafa", command = CadastrandoProduto) # Botao que abre outra janela com labels para cadastro de produto.
# botaoRegistraCompra             = Button(janela, width = 20, height = 6, text = "Registra Compra"   , bg = "#03A9F4", command = registraCompra)
botaoSair                       = Button(janela, width = 60, height = 3, text = "Sair"              , bg = "#c62828", command = sair) # Botao para sair da janela
botaoVizualizarCliente          = Button(janela, width = 60, height = 3, text = "Ver Clientes", bg = "#04B404", command = verClientes)
botaoVerProdutosTabela          = Button(janela, width = 60, height = 3, text = "Ver Produtos", bg = "#04B404", command = verProdutos)

# POSICAO DOS BOTOES USANDO PLACE
botaoCadastrarCliente.place      (x = 32, y = 180)
botaoVizualizarCliente.place     (x = 32, y = 240)
botaoCadastrarProduto.place      (x = 32, y = 300)
botaoVerProdutosTabela.place     (x = 32, y = 360)
# botaoRegistraCompra.place        (x = 340, y = 180)
botaoSair.place                  (x = 32, y = 510)

janela.mainloop()