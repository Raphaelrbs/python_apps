import os

restaurantes = ['Fome Maluca', 'Fome louca']


def exibir_nome_do_programa():
    print('AiFome\n')


def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. lista restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    os.system('clear')
    print('Finalizando o App\n')


def opcao_invalida():
    print('Opção invalida\n')
    input('Aprete uma tecla para voltar ao menu  ')


def cadastras_novo_restaurante():
    os.system('clear')
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restalraante {nome_do_restaurante} cadastrado com sucesso!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def listar_restaurantes():
    os.system('clear')
    print('Lista de restaurantes\n')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastras_novo_restaurante()
            print('Cadastra restaurante')
        elif opcao_escolhida == 2:
            listar_restaurantes()
            print('Listar restaurantes')
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
