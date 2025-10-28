import json
import os

# Caminho do arquivo onde o estoque será salvo
ARQUIVO_ESTOQUE = "estoque.json"

# Função para carregar o estoque (caso o arquivo exista)
def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, "r") as f:
            return json.load(f)
    else:
        return {}

# Função para salvar o estoque
def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, "w") as f:
        json.dump(estoque, f, indent=4)

# Carrega o estoque existente (ou cria um novo vazio)
estoque = carregar_estoque()

# Loop principal
while True:
    print('\n=== Controle de Estoque ===')
    print('1. Adicionar produto')
    print('2. Remover produto')
    print('3. Atualizar estoque')
    print('4. Ver estoque')
    print('5. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome do produto: ')
        quantidade = int(input('Quantidade: '))
        estoque[nome] = estoque.get(nome, 0) + quantidade
        salvar_estoque(estoque)
        print(f'{quantidade} unidade(s) de {nome} adicionada(s).')

    elif opcao == '2':
        nome = input('Nome do produto: ')
        if nome in estoque:
            del estoque[nome]
            salvar_estoque(estoque)
            print(f'{nome} removido do estoque.')
        else:
            print('Produto não encontrado.')

    elif opcao == '3':
        nome = input('Nome do produto: ')
        if nome in estoque:
            nova_qtd = int(input('Nova quantidade: '))
            estoque[nome] = nova_qtd
            salvar_estoque(estoque)
            print(f'Quantidade de {nome} atualizada para {nova_qtd}.')
        else:
            print('Produto não encontrado.')

    elif opcao == '4':
        print("\n--- Estoque Atual ---")
        if estoque:
            for nome, qtd in estoque.items():
                print(f'{nome}: {qtd}')
        else:
            print('Estoque vazio.')

    elif opcao == '5':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida. Tente novamente.')
