#Trabalho de POO e Linguagem de Programação
#Alunos: Fabio Koiti Tazo
#        Giovanna de Souza Régis
#        Letícia Sophia Rodrigues da Silva
#2º ano Téc. em Informática Matutino Integrado

import sys
import os

class Pessoa:
  def __init__ (self, id, estrelas):
    while True:
      try:
        self.nome = input ("DIGITE O SEU NOME COMPLETO: ")
        for y in self.nome:
          if y.isalpha() == False:
            raise ValueError
            break
            sys.exit()

      except ValueError:
        print ("POR FAVOR, UTILIZE APENAS LETRAS! VERIFIQUE AS INFORMAÇÕES FORNECIDAS E TENTE NOVAMENTE.")
        break
        sys.exit()
      try:
        self.contato = input ("DIGITE O SEU CONTATO: ")
        for y in self.contato:
          if y.isdigit() == False:
            raise ValueError
            break
            sys.exit()
      except ValueError:
        print ("POR FAVOR, DIGITE APENAS NÚMEROS! VERIFIQUE AS INFORMAÇÕES FORNECIDAS E TENTE NOVAMENTE.")
    self.id = id
    self.estrelas = estrelas
  def abrir_perfil (self):
    os.system('clear')
    print ("PERFIL DE: ", self.nome)
    print ("CONTATO: ", self.contato)
  def enviar_mensagem (self):
    mensagem = input ("DIGITE A MENSAGEM A SER ENVIADA: ")
    print = ("MENSSAGEM ENVIADA COM SUCESSO!")

class Endereco:
  def __init__(self):
    while True:
      self.logradouro = input ("DIGITE O NOME DO SEU LOGRADOURO: ")
      try:
        self.numero = input ("DIGITE O NÚMERO DA SUA RESIDÊNCIA: ")
        for y in self.numero:
          if y.isdigit() == False:
            raise ValueError
            break
            sys.exit()
      except ValueError:
        print ("POR FAVOR, DIGITE APENAS NÚMEROS! VERIFIQUE AS INFORMAÇÕES FORNECIDAS E TENTE NOVAMENTE.")
      try:
        self.bairro = input ("DIGITE O BAIRRO QUE VOCÊ RESIDE: ")
        for y in self.bairro:
          if y.isalpha() == False:
            raise ValueError
            break
            sys.exit()
      except ValueError:
        print ("POR FAVOR, DIGITE APENAS LETRAS! VERIFIQUE AS INFORMAÇÕES FORNECIDAS E TENTE NOVAMENTE.")
    self.complemento = input ("DIGITE O SEU COMPLEMENTO: (ex.: CONDOMÍNIO DAS FLORES)")
    self.cidade = input ("DIGITE A SUA CIDADE: ")
    self.cep = input ("DIGITE O SEU CEP: ")
  def cadastrarendereco (self, Endereco):
    self.Endereco ()
  def alterar_endereco (self, Endereco):
    self.Endereco ()

class Cliente (Pessoa):
  def __init__(self, id, estrelas):
    super().__init__(id, estrelas)
    self.cpf = input ("DIGITE O SEU CPF: ")
    self.endereco = Endereco()
    self.forma_pagamento = 0 
  def cancelar_pedido (self):
    print ("SEU PEDIDO FOI CANCELADO COM SUCESSO!")
  def confirmar_pedido (self):
    resposta = input ("VOCÊ DESEJA CONFIRMAR O(S) PEDIDO(S)?  ")
    if confirmar == "sim" or "SIM" or "Sim":
      print ("PEDIDO CONFIRMADO! MUITO OBRIGADE!")
      return True
    else:
      return False
  def informar_atraso (self):
    print ("ALERTA DE ATRASO ENVIADO COM SUCESSO!")
  def avaliar_entregador (self):
    avaliacao_entregador = input (float ("DIGITE A AVALIAÇÃO DO ENTREGADOR (0.0 A 5.0 ESTRELAS - DIGITAR APENAS NÚMEROS) "))
    return avaliacao_entregador
  def avaliar_restaurante (self):
    avaliacao_restaurante = input (float ("DIGITE A AVALIAÇÃO DO RESTAURANTE (0.0 A 5.0 ESTRELAS - DIGITAR APENAS NÚMEROS) "))
    return avaliacao_restaurante

cliente = Cliente ("", "")

class Entregador (Pessoa):
  def __init__(self, conducao, placa, nome, contato, id, estrelas):
    super().__init__(nome, contato, id, estrelas)
    self.conducao = conducao
    self.placa = placa
  def relatar_problema_entrega (self):
    print("PROBLEMA RELATADO COM SUCESSO. AGUARDE O CONTATO DA EMPRESA. MUITO OBRIGADE! ")
  def confirmar_entrega (self):
    print ("ENTREGA CONFIRMADA COM SUCESSO! MUITO OBRIGADE!")
  def avaliar_cliente (self):
    avaliacao_cliente = input (float) ("DIGITE A AVALIAÇÃO DO CLIENTE (0.0 A 5.0 ESTRELAS - DIGITAR APENAS NÚMEROS) ")
    print ("CLIENTE AVALIADO COM SUCESSO!")

class Funcionario (Pessoa):
  def __init__ (self, data_admissao, cargo, cpf_funcionario, nome, contato, id, estrelas):
    super().__init__(nome, contato, id, estrelas)
    self.data_admissao = data_admissao
    self.cargo = cargo
    self.cpf_funcionario = cpf_funcionario
  def liberar_pedido (self):
    confirmar = input ("VOCÊ DESEJA CONFIRMAR O(S) PEDIDO(S)?:  ")
    if confirmar == "sim" or "SIM" or "Sim":
      print ("PEDIDO CONFIRMADO! MUITO OBRIGADE!")
      return True
    else:
      return False
  def registrar_entrada (self):
    print ("ENTRADA REGISTRADA COM SUCESSO!")
  def registrar_saida (self):
    print ("SAÍDA REGISTRADA COM SUCESSO!")

class Cardapio:
  def __init__(self):
    self.cardapio=[]

  def exibir_cardapio (self):
    #self.cardapio = cardapio #não precisa dessa linha
    self.cardapio = ["SUSHI TRADICIONAL", "HOSOMAKI", "MAKIZUSHI", "TEMAKI", "URUMAKI", "NIGUIRI", "SASHIMI", "HOT FILADÉLFIA", "TEMPURÁ", "YAKISOBA TRADICIONAL", "YAKISOBA VEGANO", "HARUMAKI", "MOYASHI", "MOCHI", "MANJU"]  
    
    for x in range (len(self.cardapio)):
      print(x+1,'-', self.cardapio[x])
    print("16 - ENCERRAR PEDIDOS E PROSSEGUIR")
    a = input("DIGITE O NÚMERO CORRESPONDENTE AO SEU PEDIDO (OBS.: VOCÊ PODERÁ ESCOLHER MAIS DE UM PEDIDO DESDE SELECIONE UM DE CADA VEZ): ")
    if a == '1':
      os.system('clear')
      self.cardapio.append(sushi_tradicional)
      self.exibir_cardapio()
    elif a== '2':
      os.system('clear')
      self.cardapio.append(hosomaki)
      self.exibir_cardapio()
    elif a== '3':
      os.system('clear')
      self.cardapio.append(makizushi)
      self.exibir_cardapio()
    elif a== '4':
      os.system('clear')
      self.cardapio.append(temaki)
      self.exibir_cardapio()
    elif a== '5':
      os.system('clear')
      self.cardapio.append(urumaki)
      self.exibir_cardapio()
    elif a== '6':
      os.system('clear')
      self.cardapio.append(niguiri)
      self.exibir_cardapio()
    elif a== '7':
      os.system('clear')
      self.cardapio.append(sashimi)
      self.exibir_cardapio()
    elif a== '8':
      os.system('clear')
      self.cardapio.append(hot_filadelfia)
      self.exibir_cardapio()
    elif a== '9':
      os.system('clear')
      self.cardapio.append(tempura)
      self.exibir_cardapio()
    elif a== '10':
      os.system('clear')
      self.cardapio.append(yakisoba_tradicional)
      self.exibir_cardapio()
    elif a== '11':
      os.system('clear')
      self.cardapio.append(yakisoba_vegano)
      self.exibir_cardapio()
    elif a== '12':
      os.system('clear')
      self.cardapio.append(harumaki)
      self.exibir_cardapio()
    elif a== '13':
      os.system('clear')
      self.cardapio.append(moyashi)
      self.exibir_cardapio()
    elif a== '14':
      os.system('clear')
      self.cardapio.append(mochi)
      self.exibir_cardapio()
    elif a== '15':
      os.system('clear')
      self.cardapio.append(manju)
      self.exibir_cardapio()
    elif a== '16':
      os.system('clear')
      menu = Menu()
      menu.remover_produto_cardapio()
    else:
      os.system('clear')
      print("ERRO")
      self.exibir_cardapio() 
    #self.comanda = (a)
  #return (a)
global cardapio

cardapio = Cardapio ()

class Carrinho:
  def __init__(self):
    self.id_venda = id_venda
    self.cardapio = Cardapio()
    self.endereco_entrega = Endereco()
  def remover_produto (self):
    produto = None
  def cancelar_pedido (self):
    print ("PEDIDO CANCELADO COM SUCESSO!")
  def confirmar_pedido (self):
    confirmacao = input ("VOCÊ DESEJA CONFIRMAR O(S) PEDIDO(S)?  ")
    if confirmacao == "sim" or "SIM" or "Sim":
      print ("PEDIDO CONFIRMADO! MUITO OBRIAGADE!")
      return True
    else:
      return False

class Produtos:
  def __init__ (self, preco_produto, id_produto, tipo_ProdutoSalgado):
    self.preco_produto = preco_produto
    self.id_produto = id_produto
    self.tipo_ProdutoSalgado = True
  def cadastrar_produto (self):
    self.produto = input ("DIGITE O NOME DO PRODUTO A SER CADASTRADO: ")
    print ("PRODUTO CADASTRADO COM SUCESSO!")
  def alterar_produto (self):
    self.produto = input ("DIGITE O NOVO PRODUTO: ")
    print ("PRODUTO ALTERADO COM SUCESSO!")
  def adicionar_produto_estoque (self):
    produto_estoque = input ("DIGITE O NOME DO PRODUTO A SER ADICIONADO NO ESTOQUE: ")
    print ("PRODUTO ADICIONADO COM SUCESSO!")
  def remover_produto_estoque (self):
    produto_estoque = None

sushi_tradicional = Produtos(3.00,1,True)
hosomaki = Produtos(3.00,2,True)
makizushi = Produtos(3.50,3,True)
temaki = Produtos(5.00,4,True)
urumaki = Produtos(3.50, 5, True)
niguiri = Produtos(8.00, 6, True)
sashimi = Produtos(5.00,7, True)
hot_filadelfia = Produtos(4.00,8, True)
tempura = Produtos( 5.00, 9, True)
yakisoba_tradicional = Produtos(47.90, 10, True)
yakisoba_vegano = Produtos(48.00,11, True)
harumaki = Produtos(10.00, 12, True)
moyashi = Produtos (20.00, 13, True)
mochi = Produtos (5.00, 14, False)
manju =Produtos(6.00, 15, False)

class Menu:

  def __init__(self):
    self.menu = menu = []
    self.cardapio = Cardapio()
  def Exibir_Menu_um(self):
    global cliente
    print("QUERIDE USUARIE, POR FAVOR, PREENCHA AS INFORMAÇÕES ABAIXO PARA A REALIZAÇÃO DO SEU CADASTRO.")
    print("")
    os.system('clear')
    self.Exibir_Menu_dois()
  
  def Exibir_Menu_dois(self):
    print("1-VISUALIZAR PERFIL\n2-VISUALIZAR CARDÁPIO\n3-SAIR DO SISTEMA")
    a = input ("DIGITE O NÚMERO CORRESPONDENTE A AÇÃO DESEJADA: ")
    if a == "1":
      cliente.abrir_perfil()
      self.Exibir_Menu_dois()
    elif a == "2":
      os.system('clear')
      self.cardapio.exibir_cardapio()
    elif a == "3":
      os.system('clear')
      print("SISTEMA ENCERRADO! MUITO OBRIGADE!")
      sys.exit()
    else:
      os.system('clear')
      print("ERRO")
      self.Exibir_Menu_dois
  def Exibir_Menu_tres (self):
    print ("1-REALIZAR NOVO PEDIDO\n2-INSTRUÇÕES DE PAGAMENTO E ENTREGA")
    a = input ("DIGITE O NÚMERO CORRESPONDENTE A AÇÃO DESEJADA: ")
    if a == "1":
      os.system('clear')
      self.exibir_cardapio()
    elif a == "2":
      os.system('clear')
      self.remover_produto_cardapio()
    else:
      os.system('clear')
      print ("ERRO")
    self.Exibir_Menu_dois
  def remover_produto_cardapio (self):
    total = 0
    for x in range (len(self.cardapio.comanda)):
      total=total+self.cardapio.comanda[x].preco_produto
    os.system('clear')
    print ("O TOTAL DA SUA COMPRA É: R$", total)
    print ("OBRIGADE POR COMPRAR CONOSCO!")

menu = Menu()
menu.Exibir_Menu_um()