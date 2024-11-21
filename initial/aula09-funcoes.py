from typing import TypeVar
print("funcao")
print("funcao com parametro")
n1 = 23
n2 = 43
def somar():
    soma = n1 + n2
    print("Soma = " + str(soma))

somar()

print("")
print("funcao com parametro")
T = TypeVar("T")
def subtrair(n1: T, n2: T) -> T:
    soma = n1 - n2
    print("Subtração = " + str(soma))
    return soma

subtrair(50, 20)

print("")
print("Argumentos arbitrarios")
def textos(*n):
    print("n = ", n[0])
    print("n = ", n[1])
    print("n = ", n[2])

textos("Pedro", "Lucas", "Carlos", "Ana", "Luis")

print("")
print("Argumentos arbitrarios")
def superSoma(*num):
    soma = 0

    for n in num:
        soma += n
    print("super soma = " + str(soma))

superSoma(50, 20, 30, 10, 32)


print("")
minhaLista = [3, 43, 53, 4, 3]
print("funcao com lista como paramentro")
def superSoma(lista: list[int]):
    soma = 0

    for n in lista:
        soma += n
    print("super soma = " + str(soma))

superSoma(minhaLista)

print("")
print("valor padrao no parametro")
def getCarro(carro = "Golf"):
    print("Modelo = " + carro)

getCarro("HRV")
getCarro()