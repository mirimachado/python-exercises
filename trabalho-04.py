# questão 04
lista_de_livros = []
codigo_livros = 0
def cadastrar_livros(codigo):
    print("Bem vindo ao menu de Cadastrar livros")
    print("Código do livro: {}".format(codigo))
    nome = input("Entre com o nome do livro")
    autor = input("Entre com o autor do livro")
    editora = input("Entre com a editora do livro")
    dicionario_livro = {'codigo': codigo,
                        'nome': nome,
                        'autor': autor,
                        'editora': editora
                        }
    lista_de_livros.append(dicionario_livro.copy())
def consultar_livros():
    print("Bem vindo ao menu de consultar livros")
    while True:
        opcao_consultar = input("Escolha a opção desejada: \n" +
                                "1- Consultar todos os livros \n" +
                                "2- Consultar livros por id \n" +
                                "3- Consultar livros por autor \n" +
                                "4- Retornar \n" +
                                ">> ")
        if opcao_consultar == "1":
            print("Você escolheu a opção consultar todos os livros")
            for livro in lista_de_livros:
                for key, value in livro.items():
                    print("{}: {}".format(key, value))
        elif opcao_consultar == "2":
            print("Você escolheu a opção consultar livros por id")
            valor_desejado = int(input("Entre com o id desejado: "))
            for livro in lista_de_livros:
                if livro["codigo"] == valor_desejado:
                    for key, value in livro.items():
                        print("{}: {}".format(key, value))
        elif opcao_consultar == "3":
            print("Você escolheu a opção consultar livros por autor")
            valor_desejado = input("Entre com o autor desejado: ")
            for livro in lista_de_livros:
                if livro["autor"] == valor_desejado:
                    for key, value in livro.items():
                        print("{}: {}".format(key, value))
        elif opcao_consultar == "4":
            return  # sai da função e voltar para o main
        else:
            print("Opção inválida, tente novamente por favor!")
            continue  # volta para o início do laço
def remover_livros():
    print("Bem vindo ao menu de remover livros")
    valor_desejado = int(input("Entre com o id do livro que deseja remover: "))
    for livro in lista_de_livros:
        if livro["codigo"] == valor_desejado:
            lista_de_livros.remove(livro)
            print("Livro removido!")
print("Bem vindo ao controle de livros da M.iriã Machado de Camargo")
while True:
    opcao_principal = input("Escolha a opção desejada: \n" +
                            "1- Cadastrar livro \n" +
                            "2- Consultar livro \n " +
                            "3- Remover livro \n" +
                            "4- Encerrar programa \n" +
                            ">> ")
    if opcao_principal == "1":
        codigo_livros = codigo_livros + 1
        cadastrar_livros(codigo_livros)
    elif opcao_principal == "2":
        consultar_livros()
    elif opcao_principal == "3":
        remover_livros()
    elif opcao_principal == "4":
        break
    else:
        print("Opção inválida, tente novamente, por favor!")
        continue  # volta para o início do laço


