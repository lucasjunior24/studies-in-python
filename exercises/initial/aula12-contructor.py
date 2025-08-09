class Car:
    ligado = False
    velMax = 0
    cor = ""

    print("# self é uma referencia para propria classe, é como se fosse um this")
    def __init__(self, vel, lig, cor):
        self.velMax = vel
        self.ligado = lig
        self.cor = cor

    def mostrar(self):
        print("Cor: ", self.cor)
        print("Ligado? ", self.ligado)
        print("Velocidade Maxima: " + str(self.velMax))
        print("")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if self.ligado:
            print("Andando")
        else:
            print("Carro parado")

    def get_status(self):
        # print(str(self.ligado))
        # if self.ligado:
        #     print("Yes")
        #     return "Yes"
        # else:
        #     print("No")
        #     return "No"
        return "Yes" if self.ligado else "No"


c1 = Car(200, False, "Black")
c2 = Car(340, True, "Blue")
c3 = Car(240, False, "Red")

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.ligar()
c1.mostrar()

c1.get_status()
c2.get_status()

c1.andar()
c3.andar()