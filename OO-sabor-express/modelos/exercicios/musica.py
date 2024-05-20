class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'


    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


musica1 = Musica('Bohemian Rhapsody', 'Queen', 355)
musica2 = Musica('Imagine', 'John Lennon', 183)
musica3 = Musica('Shape of You', 'Ed Sheeran', 234)
    
Musica.listar_musicas()