# esse import foi invocada para usar a função system
import os

restaurantes = [{'nome':'Mama Mia', 'categoria':'pizzaria', 'ativo':False},
                {'nome':'Wolverine sushi', 'categoria':'Japonês', 'ativo':True},
                {'nome':'Pastel da Vovó', 'categoria':'Pastelaria', 'ativo':False}]

#estaurantes = ['Mama Mia', 'Aleaaa']

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""
        ---- 𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼 ----
        
        """)

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Altenar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('---- 𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼 ---- foi encerrado')

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
        Outputs:
        - Retorna ao menu principal
    '''
    input('\nDigite um tecla para voltar ao menu ')
    main()

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    # o comando abaixo limpa o terminal. Obs: cls só no windows
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsável pelo cadastramento de restaurantes
    
        Inputs:
            - Nome do restourante;
            - Categoria;

        Outputs:
            - Adiciona um novo restaurante à lista de restaurantes;
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante}, foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f' {'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    linha = '-' * (len(f' {'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}'))
    print(linha)
    for restaurante in restaurantes:
       nome_restaurante = restaurante['nome']
       categoria = restaurante['categoria']
       ativo = 'ativado' if restaurante['ativo'] else 'desativado'
       print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_ao_menu_principal()



def alternar_estado_do_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo( 'Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()


def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print('Cadastrar restaurante\n')
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            listar_restaurantes()
            
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
            
        elif opcao_escolhida == 4:
            finalizar_app()
                
        else:
            opcao_invalida()
            # print('Encerrar programa\n')
    except:
        opcao_invalida()      

# print(f'Você escolheu a {opcao_escolhida}.')
def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()