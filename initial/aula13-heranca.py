print("")
print("HERANÇA")
print("É quando uma classe Filho herda de outras as caracteristacas de uma classe Pai")

print("Class Pai, ou Base ou Super classe")
class NPC: 
    def __init__(self, nome, time, forca, municacao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municacao = municacao
        self.vivo = True
        self.energia = 100

    def info(self):
        print("Nome: ", self.nome)
        print("Time: ", str(self.time))
        print("Forca: ", str(self.forca))
        print("Municao: ", str(self.municacao))
        print("Vivo: ", ("Sim" if self.vivo else "Não"))
        print("Energia: ", str(self.energia))
        print("")


class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municacao = 200
        super().__init__(nome, time, self.forca, self.municacao)


class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 80
        self.municacao = 20
        super().__init__(nome, time, self.forca, self.municacao)


class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municacao = 3000
        super().__init__(nome, time, self.forca, self.municacao)

        def inf():
            super().info()