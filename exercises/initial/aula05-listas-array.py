print("")
print("# LISTAS = Array")
print(True)

carros = ["gol", "Palio", 'Classic', "Ferrari"]
print(carros)
print(carros[0]) #  primeiro elemento
print(carros[-1]) #  ultimo elemento

print("")
print("# Editando lista")

carros[2] = "Volvo"
print(carros)

print("")
print("# Adiciona novos itens lista")
carros.append("Corolla")
carros.append("UNO")
print(carros)
print(str(len(carros)) + " carros na lista")

print("")
print("# Remover itens lista")
carros.remove("Palio")
print(carros)

print("")
print("# Remover ultimo elemento da lista")

print("forma 1")
carros.pop()

print("forma 1")
del carros[0]
print(carros)

print("")
print("# Clonar uma lista")
carros2 = list(carros)
carros2.append("Palio")
carros2.append("UNO")
print(str(len(carros2)) + " carros na lista 2")
print(carros2)


print("")
print("# Fundir duas listas")
carros2 = ["Corolla","Maverique", "TOYOTA", 'Mercedes', "Tesla"]
carros3 = carros+carros2

print(str(len(carros3)) + " carros na lista 2")
print(carros3)



print("")
print("# Limpar toda a lista, deixando ela vazia")
carros.clear()
print(carros)