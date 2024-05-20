livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}

credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

# +++++++++++++++++++++++++++++++++
pessoa = {'nome': 'Alexandre Vogelsanger', 'idade': 41, 'cidade': 'São Paulo' }

pessoa['idade'] = 59      
print(pessoa['nome'], pessoa['idade'])

pessoa['profissão'] = 'músico'
print(pessoa)

del pessoa['cidade']
print(pessoa)

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")


frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
print(palavras)

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)



