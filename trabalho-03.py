# questão 03
# início da função num_pagina()
def numeroPaginas():
    print("************* Número de páginas *************")
    while True:
        try:
            paginasN = int(input("Digite a quantidade desejada de páginas: "))
            if (paginasN >= 10) and (paginasN <= 100):  # desconto 10%
                valorDoDesconto = 10
                desconto = int((valorDoDesconto / 100) * paginasN)
                return paginasN - desconto
            elif (paginasN >= 100) and (paginasN <= 1000):  # desconto de 15%
                valorDoDesconto = 15
                desconto = int((valorDoDesconto / 100) * paginasN)
                return paginasN - desconto
            elif (paginasN >= 1000) and (paginasN < 10000):  # desconto de 20%
                valorDoDesconto = 20
                desconto = int((valorDoDesconto / 100) * paginasN)
                return paginasN - desconto
            elif paginasN < 10:
                return paginasN
            else:
                print("Não é aceito pedidos nessa quantidade de páginas.")
                continue  # retorna para a pergunta
        except ValueError:
            print("Pare de digitar valores não inteiros/inválidos. ")
# FIM da função num_pagina()
# início da função escolha_servico()
def opcaoServico():
    print("************* Tipo de serviço *************")
    while True:
        servicoEscolhido = input("Digite a opção de serviço desejada: \n" +
                                 "a - DIG - Digitalização \n" +
                                 "b - ICO - Impressão colorida \n" +
                                 "c - IPB - Impressão Preto & Branco \n" +
                                 "d - FOT - Fotocópia \n" +
                                 ">> ")
        if servicoEscolhido == "a":
            return 1.10
        elif servicoEscolhido == "b":
            return 1.00
        elif servicoEscolhido == "c":
            return 0.40
        elif servicoEscolhido == "d":
            return 0.20
        else:
            print("Digite uma opção válida, por favor!")
            continue
# FIM da função escolha_servico()
# início da função servico_extra()
def servicoExtra():
    print("************* Serviços extras *************")
    acumulador = 0
    while True:
        pedidoextra = input("Digite o serviço extra desejado: \n" +
                            "a - Encadernação simples - R$ 10,00 \n" +
                            "b - Encadernação capa dura - R$ 25,00 \n" +
                            "c - Não desejo mais nada \n")
        if pedidoextra == "c":
            return acumulador
        elif pedidoextra == "b":
            acumulador = acumulador + 25
            continue
        elif pedidoextra == "a":
            acumulador = acumulador + 10
            continue
        else:
            print("Digite uma opção váldia, por favor!")
# FIM da função servico_extra()
# início do main
print("***** Bem vindo à copiadora da Miriã Machado de Camargo *****")
paginas = numeroPaginas()
opcao = opcaoServico()
extra = servicoExtra()
total = (paginas * opcao) + extra
print("O total ficou: R$ {:.2f} R$ (Quantidade de pág: R$ {:.2f}, Serviço: R$ {:.2f}, Extra: R$ {:.2f})".format(total,paginas,opcao,extra))