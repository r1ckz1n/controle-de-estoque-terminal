import json

try:
    with open("estoque.json", "r") as f:
        estoque = json.load(f)
except FileNotFoundError:
    estoque = {}

estoque = {}

while True:
    print('\n=== Controle de Estoque ===')
    print('1. Adicionar produto')
    print('2. Rmover produto')
    print('3. Atualizar estoque')
    print('4. Ver estoque')
    print('5. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome do produto: ')
        quantidade = int(input('Quantidade:'))
        estoque[nome] = estoque.get(nome, 0) + quantidade
        print(f'{quantidade} unidade(s) de {nome} adidiconado(s).')

    elif opcao == '2':
        nome = input('Nome do produto: ')
        if nome in estoque:
            del estoque[nome]
            print(f'{nome} removido do estoque. ')
        else:
            print('Produto não encontrado.')

    elif opcao == '3':
        nome = input('Nome do produto: ')
        if nome in estoque:
            nova_qtd = int(input('Nova quantidade: '))
            estoque[nome] = nova_qtd
            print(f'Quantidade de {nome} atualizado para {nova_qtd}.')

    elif opcao == '4':
        print("\n--- Estoque Atual ---")
    if estoque:
        for nome, qtd in estoque.items():
            print(f'{nome}: {qtd}')
    else:
        print('Estoque vazio.')
    break

else:
    print("Opção inválida. Tente novamente.")
