carros = ["gol", "Palio", 'Classic', "Ferrari"]
carros2 = ["Corolla","Maverique", "TOYOTA", 'Mercedes', "Tesla"]
carros3 = carros+carros2

print("")
print("# CONDICIOANAIS IF ELIF ELSE")
print(str(len(carros3)) + " carros na lista ")

dinheiro = 300

if(len(carros3) > 10 and dinheiro > 200):
    print("# A mais de 10 carros")
elif(len(carros3) > 4 or dinheiro < 200):
    print("# A mais de 4 carros")
elif(len(carros3) > 4 or (dinheiro >= 100 and dinheiro < 500)):
    print("# A mais de 4 carros e 300 reais")
elif(len(carros3) >= 1):
    print("# A mais de 1 carro")
else:
    print("# Não a nenhum carro")

print("")
print("# Laços de repetições")
print("# percorrendo array")
for carro in carros:
    if(carro == "Ferrari"):
        print("Meu carro é: ", carro)


print("")
print("# percorrendo string")
for letra in "Maverique":
    print(letra)
    if(letra == "v"):
        print("Letra V: ", letra)