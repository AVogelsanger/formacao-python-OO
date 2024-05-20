class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano de publicação: {self._ano_publicacao}'
    
    def emprestar(cls):
        cls._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis


livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

print(livro1)
print(livro2)


livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f'Antes de emprestar: Livro disponível? {livro3._disponivel}')
livro3.emprestar()
print(f'Depois de emprestar: Livro disponível? {livro3._disponivel}')

Livro.livros = [livro1, livro2, livro3]