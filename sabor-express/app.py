import os

# A baixo o dicionario com os nomes dos restaurantes sua categoria e se esta ativo ou não.
restaurantes = [{'nome': 'Fome Maluca', 'categoria': 'amburgueria', 'Ativo': False},
                {'nome': 'Fome Suprema', 'categoria': 'amburgueria', 'Ativo': True},
                {'nome': 'Fome Louca', 'categoria': 'amburgueria', 'Ativo': False},
                ]


# A baixo exibe o nome do Aplicatiovo
def exibir_nome_do_programa():
    print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨\n')


# A baixo exibe as opções para o usuario
def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. lista restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


# A Baixo função definida para finalizar o Aplicativo opção 4 mostrada para o usuario
def finalizar_app():
    exibir_subtitulo('Finalizar app')


# A Baixo função definida para voltar a tela inicial de escolha
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu  ')
    main()


# A Baixo função definida para caso usuario digite uma opção invalida
def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu_principal()


# A Baixo função definida limpa a tela, exibe um texto e adiciona uma linha em branco.
def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()


def cadastras_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(
        f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')

    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['Ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo} ')

    voltar_ao_menu_principal()


# A baixo mostra o bloco de opção que sera exibida na tela inicial para o usuario
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastras_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


# A baixo foi definido a função main(principal) e mostra a tela principal para o usuario e as opções abaixo para sua escolha.
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
