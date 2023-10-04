#class mae
#class filho - usa o super() para vincula com a mae]
#precisa usar todos os atributos da super, ele não aceita
#no nivel de hieraquia puxa a de cima 

class Veiculo: # super classe
    def __init__(self,marca,modelo,placa):
        self.marca=marca
        self.modelo=modelo
        self.placa=placa

    def exibir(self): #metodo generalizado
        print(self.marca)
        print(self.modelo)
        print(self.placa)



class Carro(Veiculo): # class filho - herença coloca a class mar dentro dos ()
    def __init__(self,marca,modelo,placa,portas):
        super().__init__(marca,modelo,placa) # executa a super class
        self.portas=portas

    def exibir(self):
        super().exibir()# chama o metodo do super class
        print(self.portas)

class Moto(Veiculo):
    def __init__(self,marca,modelo,placa,bagageiro):
        super().__init__(marca,modelo,placa)
        self.bagageiro=bagageiro
    
    def exibir(self):
        super().exibir()
        print(self.bagageiro)




print('Carro')
carro1= Carro ('ford', 'ka', 2010, 4)
carro1.exibir()

print('\nMoto')
moto1 = Moto ('honda', 'gf','dfg-344', True)
moto1.exibir()