#lista com tuplas das 10 primeiras moedas do mercado cripto por capitalização em Abril de 2022:
moedas = ('bitcoin', 'ethereum', 'tether', 'bnb',
          'USDC', 'solana', 'xrp', 'luna',
          'cardano', 'TerraUSD')

print('=*' * 15)
print(f'Lista das top 10 moedas por capitalização: {moedas}')
print('=*' * 15)

capitalizacao_moedas = {
    'bitcoin': '752,959,646,050',
    'ethereum': '352,470,171,043',
    'tether': '83,159,489,750',
    'bnb': '66,096,668,304',
    'USDC': '49,393,341,586',
    'solana': '32,608,552,871',
    'xrp': '30,783,556,729',
    'luna': '29,613,021,067',
    'cardano': '28,322,558,873',
    'TerraUSD': '19,118,866,395'
}

while True:
    duvidacap = input("Deseja saber o valor de capitalização de alguma moeda do top 10 em abril de 2022? (sim ou não): ").lower()

    if duvidacap == "não":
        exit()
    elif duvidacap == "sim":
        print(f'Moedas disponíveis para consulta: {", ".join(moedas)}')

        opcaoMoeda = input("Digite o nome da moeda conforme a lista anterior ou digite 'não': ").lower()

        if opcaoMoeda == 'não':
            exit()
        elif opcaoMoeda in capitalizacao_moedas:
            print(f'A capitalização hoje da {opcaoMoeda.capitalize()} é de US${capitalizacao_moedas[opcaoMoeda]}')
        else:
            print('Não entendi. Digite corretamente o nome da moeda.')
    else:
        print('Resposta inválida. Digite "sim" ou "não".')
