class Estudante:

    def __init__(self, id, nome, nota1, nota2):
        self.id = id
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2) / 2 #Calculo média