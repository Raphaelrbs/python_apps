import os

restaurantes = [{'nome': 'Fome Maluca', 'categoria': 'amburgueria', 'Ativo': False},
                {'nome': 'Fome Suprema', 'categoria': 'amburgueria', 'Ativo': True},
                {'nome': 'Fome Louca', 'categoria': 'amburgueria', 'Ativo': False},
                ]


def exibir_nome_do_programa():
    print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨\n')


def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. lista restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu  ')
    main()


def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()


def cadastras_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restalraante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['Ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo} ')

    voltar_ao_menu_principal()


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


def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
