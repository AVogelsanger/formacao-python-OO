print('-Ⓟ ⓨ ⓣ ⓗ ⓞ ⓝ  ⓝ ⓐ   Ⓔ ⓢ ⓒ ⓞ ⓛ ⓐ   ⓓ ⓔ   Ⓟ ⓡ ⓞ ⓖ ⓡ ⓐ ⓜ ⓐ ⓒ̧ ⓐ̃ ⓞ   ⓓ ⓐ   Ⓐ ⓛ ⓤ ⓡ ⓐ-')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

print(f'Meu nome é {nome} e tenho {idade} anos.')

print('A','L','U','R','A',sep='\n')

import math

pi_arredondado = math.pi

print(f'O valor arredondado de pi é: {pi_arredondado:,.2f}')


def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)
