# questão 01
print('Bem-vindo à Loja da Miriã Machado de Camargo')
# aqui estão as variáveis de entrada
valor_Unitario = int(input('Digite o valor unitário do produto: '))
quantidade_Do_Produto = int(input('Digite a quantidade do produto: '))
valor_multiplicado = valor_Unitario * quantidade_Do_Produto

##############

# início das condições de desconto

if valor_multiplicado < 1000:
    desconto = 1 * valor_Unitario
    print('Não tem desconto para este valor!')
    print('O valor SEM desconto fica: {}'.format(valor_multiplicado))

elif (valor_multiplicado >= 1000) and (valor_multiplicado < 3000):
    valorDoDesconto = 3
    desconto = int((valorDoDesconto / 100) * valor_multiplicado)
    valor_Final = valor_multiplicado - desconto
    print("O valor COM desconto fica: R$ {:.2f}".format(valor_Final))
    print('O valor SEM desconto fica: R$ {:.2f}'.format(valor_multiplicado))
elif (valor_multiplicado >= 3000) and (valor_multiplicado < 5000):
    valorDoDesconto = 5
    desconto = int((valorDoDesconto / 100) * valor_multiplicado)
    valor_Final = valor_multiplicado - desconto
    print("O valor COM desconto fica: R$ {:.2f}".format(valor_Final))
    print('O valor SEM desconto fica: R$ {:.2f}'.format(valor_multiplicado))
elif valor_multiplicado >= 5000:
    valorDoDesconto = 8
    desconto = int((valorDoDesconto / 100) * valor_multiplicado)
    valor_Final = valor_multiplicado - desconto
    print("O valor COM desconto fica: R$ {:.2f}".format(valor_Final))
    print('O valor SEM desconto fica: R$ {:.2f}'.format(valor_multiplicado))
else:
    print('Encerrando o programa...')