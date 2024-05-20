class Pessoa:
    pessoas = []

    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = int(idade)
        self._profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._profissao}'

    @classmethod
    def listar_pessoas(cls):
        print(f'{'Nome'.ljust(18)} | {'Old'} | {'Profissão'}')
        for pessoa in cls.pessoas:
            print(f'{pessoa._nome.ljust(18)} | {pessoa._idade} | {pessoa._profissao}')

    def aniversario(self):
        self._idade += 1
    
    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}.'
        else:
            return f'Olá, sou {self._nome}!'
        

alexandre = Pessoa('Alexandre', 41, 'Dev')
rosa = Pessoa('Rosa Maria', '75', 'Esteticista') 


# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')

Pessoa.listar_pessoas()
pessoa1.aniversario()
alexandre.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(alexandre)
print(alexandre.saudacao)