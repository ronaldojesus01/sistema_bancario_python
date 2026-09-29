print('=' * 50, 'BANCO RONY', '=' * 50)

saldo = 0

while True:
    print('Escolha uma opção:')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Fazer Pix')
    print('4 - Consultar saldo')
    print('5 - Sair')

    while True:
        try:
            opcao = int(input('Digite a opção: '))
        except ValueError:
            print('Digite um número válido!')
            continue
        if opcao <= 0 or opcao > 4:
            print('Opção inválida!')
            continue
        break

    if opcao == 1:
        print('Legal! Vamos fazer um depósito')

        while True:
            try:
                dep = float(input('Valor do pepósito: RS '))
            except ValueError:
                print('Valor inválido!')
                continue
            if dep <= 0:
                print('Valor inválido!')
                continue
            else:
                print('Valor depositado com sucesso')
                saldo += dep
                saldo = round(saldo, 2)
                print(f'Saldo atual: {saldo}')
            break
        continue
    elif opcao == 2:
        print('Legal! Vamos fazer um saque')

        while True:
            try:
                sacar = float(input('Valor do saque: RS '))
            except ValueError:
                print('Valor inválido!')
                continue
            if sacar <= 0:
                print('Valor inválido!')
                continue
            elif sacar > saldo:
                print('Saldo insuficiente')
                continue
            else:
                print('Saque realizado com sucesso')
                saldo -= sacar
                saldo = round(saldo, 2)
                print(f'Saldo atual: {saldo}')
            break
        continue
    elif opcao == 3:
        print('Lega! Vamos fazer um pix')

        while True:
            try:
                chave_pix = input('Chave pix: ')
            except ValueError:
                print('Valor inválido')
                continue
            break

            if len(chave_pix) < 10:
                print('Pix inválido')
                continue

        while True:
            try:
                valor_pix = float(input('Valor do pix: RS '))
            except ValueError:
                print('Valor inválido')
                continue
            if 0 >= valor_pix > 1000000000:
                print('Valor inválido')
                continue
            else:
                print('Pix realizado com sucesso')
                saldo -= valor_pix
                print(f'Saldo atual: {saldo}')
            break
        continue
    if opcao == 4:
        print(f'Seu saldo é RS{saldo}')
        continue
    if opcao == 5:
        print('Saindo...')
        print('Programa encerrado')
    break