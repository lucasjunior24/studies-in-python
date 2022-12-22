print("")
print("# Valores bool true e false")
print(True)

print("# gerando Valores booleanos por expressoes")
meuBool = 10 > 15
print(meuBool)

print("# CONVERTENDO Valores para booleanos")
print("# Quando tem valores na string ao converter para bool, ele retorna true")
meuBool = "10 > 15"
print(bool(meuBool))

# meuBool2 = ""
meuBool = ""

print("")
print("# testando bool em if")
print(bool(meuBool))
if meuBool:
    print("Tem texto")
else:
    print("Não tem texto")

print("")
print("# Qualquer valor igual a zero retorna False")
print(bool(0))
print(bool(1))
print(bool(44353))