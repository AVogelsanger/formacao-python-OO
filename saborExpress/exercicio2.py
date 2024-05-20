num = input('Digite um número: ')
num = int(num)

if num % 2 == 0:
    print('par')
else:
    print('ímpar')     


# ======================================
idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Criança')
elif idade <= 18:
    print('Adolescente')
else:
    print('Adulto')    

# ========================================

nome = input('Digite seu nome: ')
senha = input('Senha: ')

if nome == 'Alexandre' and senha == 'MarioBros94&':
    print('acesso permitido')
else:
    print('Acesso negado.')

# =========================================

x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('o ponto está localizado no eixo ou origem')    