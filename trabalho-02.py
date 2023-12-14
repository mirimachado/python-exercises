# questão 02

print("Bem vindo à Loja de Gelados da Miriã Machado de Camargo")
print("----------------------Cardápio----------------------")
print("-------| Tamanho | Cupuaçu (CP) | Açaí (AC) |-------")
print("-------|    P    |   R$ 10,00   |  R$ 12,00 |-------")
print("-------|    M    |   R$ 15,00   |  R$ 17,00 |-------")
print("-------|    G    |   R$ 19,00   |  R$ 21,00 |-------")
print("----------------------------------------------------")
contador = 0
while True:
    tamanhoEscolhido = (input("Digite o tamanho do seu interesse: "))
    if tamanhoEscolhido != "P" and tamanhoEscolhido != "G" and tamanhoEscolhido != "M":
        print("Este tamanho não é válido. Digite corretamente. ")
        continue

    saborEscolhido = (input("Digite o sabor do seu interesse: "))
    if saborEscolhido != "AC" and saborEscolhido != "CP":
        print("Este sabor não é válido. Digite corretamente. ")
        continue

    if saborEscolhido == "AC" and tamanhoEscolhido == "P":
        print("Você escolheu Açaí no tamanho P")
        contador = contador + 12

    elif saborEscolhido == "AC" and tamanhoEscolhido == "M":
        print("Você escolheu Açaí no tamanho M")
        contador = contador + 17

    elif saborEscolhido == "AC" and tamanhoEscolhido == "G":
        print("Você escolheu Açaí no tamanho G")
        contador = contador + 21

    elif saborEscolhido == "CP" and tamanhoEscolhido == "P":
        print("Você escolheu Cupuaçu no tamanho P")
        contador = contador + 10

    elif saborEscolhido == "CP" and tamanhoEscolhido == "M":
        print("Você escolheu Cupuaçu no tamanho M")
        contador = contador + 15

    elif saborEscolhido == "CP" and tamanhoEscolhido == "G":
        print("Você escolheu Cupuaçu no tamanho G")
        contador = contador + 19

        print(contador)

    pedir_mais_uma_vez = input("Deseja pedir mais alguma coisa? (S/outra tecla para sair): ")
    if pedir_mais_uma_vez == "S":
       continue
    else:
        print("O valor final para ser pago fica: R${:.2f}".format(contador))
        break