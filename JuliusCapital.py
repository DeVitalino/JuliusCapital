import time

# Valores:
preco_bitcoin = 637705.65
precofut_bitcoin_lucro = 850000
precofut_bitcoin_prejuiso = 430000

preco_ethereum = 19432.41
precofut_ethereum_lucro = 35000
precofut_ethereum_prejuiso = 12000

# Funções para cálculo de lucro e prejuízo
def calcular_lucro(preco_atual, preco_futuro, investimento):
    return (preco_futuro - preco_atual) * (investimento / preco_atual)

def calcular_prejuizo(preco_atual, preco_futuro, investimento):
    return (preco_atual - preco_futuro) * (investimento / preco_atual)

# Função para exibir o perfil do investidor
def obter_perfil():
    while True:
        perfil = input('Você é do tipo "Arriscado", "Conservador" ou "Mediano"? ').strip().lower()
        if perfil in {'arriscado', 'conservador', 'mediano'}:
            return perfil
        else:
            print('Opção inválida. Por favor, escolha entre "Arriscado", "Conservador" ou "Mediano".')

# Função para calcular e exibir os lucros e prejuízos
def calcular_investimento(moeda, preco_atual, preco_futuro_lucro, preco_futuro_prejuiso):
    while True:
        try:
            capital = float(input(f'Quanto você investiria em {moeda}? R$ '))
            if capital >= 0:
                break
            else:
                print('Por favor, insira um valor maior ou igual a R$ 0.')
        except ValueError:
            print('Valor inválido. Insira um número.')

    lucro = calcular_lucro(preco_atual, preco_futuro_lucro, capital)
    prejuizo = calcular_prejuizo(preco_atual, preco_futuro_prejuiso, capital)

    print(f'No melhor cenário, seu lucro seria de R${round(lucro, 2)}')
    print(f'No pior cenário, seu prejuízo seria de R${round(prejuizo, 2)}')

# Função principal para executar o programa
def simulador_investimentos():
    # Conhecendo o usuário
    print('''Olá, Usuário! Seja Bem-vindo ao Julius!
Sua calculadora de Investimentos.''')

    nome = input('Antes de prosseguirmos, gostaria de saber o seu nome: ')
    print(f'Prazer, {nome}. Mas cada segundo aqui me custa 25 centavos.')

    while True:
        try:
            idade = int(input('Agora, fala logo a sua idade, porque tempo é dinheiro e eu não tô aqui à toa! '))
            if idade > 0:
                break
            else:
                print('Idade inválida. Por favor, digite uma idade positiva.')
        except ValueError:
            print('Idade inválida. Por favor, digite um número.')

    perfil = obter_perfil()
    time.sleep(2)

    # Recomendações de acordo com o perfil
    if perfil == 'arriscado':
        print('Você é do tipo que arrisca tudo? Então, criptomoedas são uma boa opção para você!')
        print('Mas não venha chorar depois se perder tudo, porque eu não vou te emprestar um centavo, hein!')
        time.sleep(2)
        confi_cripto = input('Vai se jogar em criptomoedas? (sim/não) ').strip().lower()
        if confi_cripto == 'sim':
            moeda = input('Você vai investir em BitCoin ou Ethereum? ').strip().lower()

            if moeda in {'bitcoin', 'bitco'}:
                print(f'O BitCoin hoje está valendo cerca de R$ {preco_bitcoin}. Vamos fazer os cálculos.')
                calcular_investimento('BitCoin', preco_bitcoin, precofut_bitcoin_lucro, precofut_bitcoin_prejuiso)

            elif moeda in {'ethereum', 'etherum'}:
                print(f'O Ethereum hoje está valendo cerca de R$ {preco_ethereum}. Vamos fazer os cálculos.')
                calcular_investimento('Ethereum', preco_ethereum, precofut_ethereum_lucro, precofut_ethereum_prejuiso)

            else:
                print('Moeda não reconhecida. Por favor, escolha entre Bitcoin e Ethereum.')
        else:
            print('Ok, parece que você não está pronto para o risco das criptos. Vai de renda fixa mesmo!')

    elif perfil == 'conservador':
        print('Você é mais conservador? Talvez fundos de renda fixa ou títulos do governo sejam o melhor para você!')
        print('Eu ficaria tranquilo, você vai dormir bem à noite... ou não, porque dinheiro parado não faz graça.')
        time.sleep(2)

        

    elif perfil == 'mediano':
        print('Você é um investidor mediano? Uma boa mistura de ações estáveis e criptomoedas pode ser o ideal!')
        print('Você sabe, sempre tem um "pá" ou "bum" no mercado, então se prepare, mas sem muito estresse!')
        time.sleep(2)

simulador_investimentos()
