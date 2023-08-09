class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}.")

# Criando objetos da classe Estudante
estudante1 = Estudante("João", 20, "Engenharia")
estudante2 = Estudante("Maria", 22, "Medicina")
estudante3 = Estudante("Pedro", 19, "Ciência da Computação")

# Usando o método apresentar para exibir informações dos estudantes
estudante1.apresentar()  # Saída: Olá, meu nome é João, tenho 20 anos e estou cursando Engenharia.
estudante2.apresentar()  # Saída: Olá, meu nome é Maria, tenho 22 anos e estou cursando Medicina.
estudante3.apresentar()  # Saída: Olá, meu nome é Pedro, tenho 19 anos e estou cursando Ciência da Computação.