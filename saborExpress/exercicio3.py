numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['José', 'Jacó', 'Isaque']
ano = [1983, 2024]

soma = 0
for num in numeros:
    if num % 2 == 1:
        print(num)
        soma = soma + num

print(soma)
print()

for num in range(numeros[9], 0, -1):
    #num = numeros[9] - num
    print(num)
print()


numeroUser = input('Informe um número: ')
for i in range(11):
    result = int(numeroUser) * i
    print(numeroUser, ' x ', i, '=', result)
print()

soma = 1
try:
    for num in numeros:
        soma += num
    print(soma)
except Exception as e:
    print(f'Ocorreu um erro: {e}')    
print()    
    

lista_valores = [15, 20, 25, 30]
soma_valores = 0
try:
    for valor in lista_valores:
        soma_valores += valor
        media = soma_valores / len(lista_valores)
        print('A média dos valores é: ', media)
except Exception as e:
    print(f'Ocorreu um erro: {e}')        