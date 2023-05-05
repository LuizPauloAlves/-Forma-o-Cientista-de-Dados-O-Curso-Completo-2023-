while True:
    peso = int(input("Digite o Peso da carga:"))
    if peso == 0:
        break
    elif peso <= 10:
        print("valor R$50,00")
    elif peso > 10 and peso <= 20:
        print('valor R$80,00')
    else:
        print('Não é aceito')
