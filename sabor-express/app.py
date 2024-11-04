import os

# Abaixo o dicionário com os nomes dos restaurantes, sua categoria e se estão ativos ou não.
restaurantes = [{'nome': 'Fome Maluca', 'categoria': 'hamburgueria', 'Ativo': False},
                {'nome': 'Fome Suprema', 'categoria': 'hamburgueria', 'Ativo': True},
                {'nome': 'Fome Louca', 'categoria': 'hamburgueria', 'Ativo': False}]


# Abaixo exibe o nome do Aplicativo
def exibir_nome_do_programa():
    print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨\n')


# Abaixo exibe as opções para o usuário
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')


# Abaixo função definida para finalizar o Aplicativo (opção 4 mostrada para o usuário)
def finalizar_app():
    exibir_subtitulo('Finalizar app')


# Abaixo função definida para voltar à tela inicial de escolha
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu  ')
    main()


# Abaixo função definida para caso o usuário digite uma opção inválida
def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()


# Abaixo função definida limpa a tela, exibe um texto e adiciona uma linha em branco.1
def exibir_subtitulo(texto):
    os.system('cls') # se for rodar em linux mudar o comando para ('clear')
    linha = '*' * (len(texto) + 4 )
    print(linha)
    print(texto)
    print(linha)
    print()


# A Função abaixo definida realiza o cadastro dos novos restaurantes passados pelo usuário.
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')

    voltar_ao_menu_principal()


# A Função abaixo definida mostra os restaurantes cadastrados pelos usuários
def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status' )

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['Ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')

    voltar_ao_menu_principal()


# A Função abaixo definida altera o estatos dos restaurantes casdastrados para ativado ou desativado.
def alternar_status_do_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    voltar_ao_menu_principal()


# Abaixo mostra o bloco de opções que será exibido na tela inicial para o usuário
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


# A baixo foi definido a função main(principal) e mostra a tela principal para o usuario e as opções abaixo para sua escolha.
def main():
    os.system('cls') # se for rodar em linux mudar o comando para ('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
