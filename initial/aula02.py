import random


print("Tipos númericos, random e operações de Casting");
print("");
print("Conversão de Tipos");
num_inteiro = 3
num_float = 8.43
num_complexo = 5j

tipoInt = int(num_float) #converte para inteiro
tipoString = str(tipoInt) #converte para String
tipoFloat = float(tipoString) #converte para Floart

print("Valor: " + str(num_inteiro) + " - Tipo: " + str(type(num_inteiro)))
print("Valor: " + str(tipoFloat) + " - Tipo: " + str(type(tipoFloat)))
print("Valor: " + str(num_complexo) + " - Tipo: " + str(type(num_complexo)))

print("");
print("Tipo ramdom");

print("Gerar um valor aleatorio entre números");
numRandom = random.randrange(0, 40)

print("Valor: " + str(numRandom) + " - Tipo: " + str(type(numRandom)))

print("");
print("Gerar um array de valores aleatorios");
ArrayDeRandom =[ # List / Array
    random.randrange(0, 40),
    random.randrange(0, 40),
    random.randrange(0, 40),
    random.randrange(0, 40),
    random.randrange(0, 40),
    random.randrange(0, 40)
]
print("Gerado array de 6 valores aleatorios");

print("Item 1 - Valor: " + str(ArrayDeRandom[0]) + " - Tipo: " + str(type(ArrayDeRandom[0])))
print("Item 2 - Valor: " + str(ArrayDeRandom[1]))
print("Item 3 - Valor: " + str(ArrayDeRandom[2]))
print("Item 4 - Valor: " + str(ArrayDeRandom[3]))
print("Item 5 - Valor: " + str(ArrayDeRandom[4]))
print("Item 6 - Valor: " + str(ArrayDeRandom[5]))
print("Valor: " + str(ArrayDeRandom) + " - Tipo: " + str(type(ArrayDeRandom)))

ArrayDeRandom.reverse()
print("Valor: " + str(ArrayDeRandom) + " - Tipo: " + str(type(ArrayDeRandom)))


