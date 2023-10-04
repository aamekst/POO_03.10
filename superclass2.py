class Pessoa:
    def __init__(self,nome,idade,rg,cpf):
        self.nome=nome
        self.idade=idade
        self.rg=rg
        self.cpf=cpf
    
    def exibir(self):
        print(self.nome)
        print(self.idade)
        print(self.rg)
        print(self.cpf)


class Aluno(Pessoa):
    def __init__(self,nome,idade,rg,cpf,ra): # se for add
        super().__init__(nome,idade,rg,cpf)#mesmo atributo da mae
        self.ra=ra
    def exibir(self):#sem construtor, usa o msm da super, so usa se for acrescent algo a mais
        super().exibir()
        print(self.ra)
   

aluno1 = Aluno('alana', 20, '391229151', '4332009983', '2300143')
aluno1.exibir()
print(aluno1.nome)