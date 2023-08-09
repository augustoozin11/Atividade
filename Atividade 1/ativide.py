class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Exemplo de uso
estudante1 = Estudante("Augutoo", 20)
estudante2 = Estudante("Maria", 22)

estudante1.apresentar()  # Saída: Olá, meu nome é João e tenho 20 anos.
estudante2.apresentar()  # Saída: Olá, meu nome é Maria e tenho 22 anos.