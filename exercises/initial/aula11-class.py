class Car:
    velMax =0
    ligado=False
    cor="black"

    def get_status(ligado):
        return "Yes" if ligado else "No" 
    status = get_status(ligado)

c1 = Car()
c2 = Car()
c3 = Car()

c2.cor = "red"
c2.ligado = True

c2.velMax = 120

print(c1.ligado)
print(c1.status)
print(c2.ligado)
print(c2.status)