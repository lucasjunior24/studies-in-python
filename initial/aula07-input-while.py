import os

print("# Input")
print("# variavel salva do tipo string")
# nome=input("Digite um nome: ")
# print("Nome digitado: " + nome)

print("")
print("# operacoes com Input")
print("# Limpar tela windows")
os.system('cls')
# print("# Limpar tela linux")
# os.system('clear')

# n1=int(input("Digite um numero: "))
# n2=int(input("Digite outro numero: "))
# soma = n1 + n2
# print("Soma dos valores é: " + str(soma))


print("")
print("# WHILE") # ENQUANTO
i=0
while i<=9:
    print(i)
    i+=1
    if (i >= 5):
        break
print("Fim do loop")


print("")
print("# WHILE em arrays") # ENQUANTO
carros = ["Corolla","Maverique", "TOYOTA", 'Mercedes', "Tesla"]
i=0
while i < len(carros):
    print(carros[i])
    i+=1
print("\nFim do loop")