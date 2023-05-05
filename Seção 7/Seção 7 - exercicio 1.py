def amplitude(list):
    M = max(list)
    m = min(list)
    amp = M-m
    return amp

lista = [-5,1,2,3,4,5,6,7,8,9]
valor = amplitude(lista)
print(valor)