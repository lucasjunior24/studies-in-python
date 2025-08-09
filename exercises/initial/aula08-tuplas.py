print("")
print("# tuplas")

carrosLista = ["gol", "Palio", 'Classic', "Ferrari"] # lista

print("# tuplas não suporta adição ou modificação de itens")
carros = ("gol", "Palio", 'Classic', "Ferrari")
for carro in carros:
    print("Meu carro é: ", carro)

print("# é necessario converter a tupla para lista para poder modificala ")

print("")
print("# Convertendo tuplas em lista")
carrosLista = list(carros)
print(carrosLista)

carrosLista[2] = "HRV"
print(carrosLista)

print("")
print("# Convertendo lista em tuplas de volta")
carros = tuple(carrosLista)
print(carros)



print("")
print("# Matrizes")
carros = [
            ["Modelo", ["HRV"]], 
            ["Fabricante", ["Honda", "Fiat"]], 
            ["Ano", ["2016"]]
         ]
print(carros[1][0])
print(carros[1][1])
print(carros[1][1][1])


carros = [
            ["Modelo", "HRV"], 
            ["Fabricante", "Honda"], 
            ["Ano", 2016]
         ]
         
print(carros[1][0])
print(carros[1][1])

carros[2][1] = 2022


for linha, coluna in carros:
    print("Linha: " +  linha  + " | Coluna: "+ str(coluna))

print("")
print("# Adicionado elementos a Matriz ")
carros.append(["Cor", "Prata"])
print(carros)

