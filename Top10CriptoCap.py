# Capitalização-cripto-com-tuplas-em-abril-22
Lista com tuplas das 10 primeiras moedas do mercado cripto por capitalização em Abril de 2022:
  
moedas = ('bitcoin', 'ethereum', 'tether', 'bnb',
          'USDC', 'solana', 'xrp', 'luna',
          'cardano', 'TerraUSD')
print('=*'*15)
print(f'Lista das top10 moedas por capitalização: {moedas}')
print('=*'*15)
print(f'As primeiras 5 moedas por capitalização são: {moedas[0:5]}')
print('=*'*15)
print(f'As ultimas 3 moedas por capitalização são: {moedas[-3:]}')
print('=*'*15)
print(f'A binance coin - BNB está na {moedas.index("bnb")}º posição \n')

capitalização = ('752,959,646,050', '352,470,171,043', '83,159,489,750', '66,096,668,304',
                 '49,393,341,586', '32,608,552,871', '30,783,556,729',
                 '29,613,021,067', '28,322,558,873', '19,118,866,395')
print("Deseja saber o valor de capitalização de alguma moeda do top 10 em abril de 2022?")
duvidacap = input("sim ou não:")

while duvidacap == "sim":
    opcaoMoeda = input("digite o nome da moeda conforme a lista anterior ou digite 'não':")

    if duvidacap == "nao":
        exit()
    elif opcaoMoeda == 'bitcoin':
        print(f' A capitalização hoje do bitcoin é de US${capitalização[0]} ')
    elif opcaoMoeda == 'ethereum':
        print(f' A capitalização hoje do ethereum é de US${capitalização[1]}')
    elif opcaoMoeda == 'tether':
        print(f' A capitalização hoje do Dólar Tether é de US${capitalização[2]}')
    elif opcaoMoeda == 'bnb':
        print(f' A capitalização hoje da BNB é de US${capitalização[3]}')
    elif opcaoMoeda =='USDC':
        print(f' A capitalização hoje do USDC é de US${capitalização[4]}')
    elif opcaoMoeda == 'solana':
        print(f' A capitalização hoje da Solana é de US${capitalização[5]}')
    elif opcaoMoeda == 'xrp':
        print(f' A capitalização hoje da xrp é de US${capitalização[6]}')
    elif opcaoMoeda == 'luna':
        print(f' A capitalização hoje da luna é de US${capitalização[7]}')
    elif opcaoMoeda == 'Cardano':
        print(f' A capitalização hoje da Cardano é de US${capitalização[8]}')
    elif opcaoMoeda == 'Terrausd':
        print(f' A capitalização hoje da terrausd é de US${capitalização[9]}')
    elif opcaoMoeda == 'não':
        exit()
    else:
        print('Não entendi. Digite corretamente o nome da moeda.')
        
        
