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
        if opcao <= 0 or opcao > 5:
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
            if dep <= 0 or dep > 1000000000:
                print('O depósito não pode ser menor que zero ou igual a zero e nem maior que 1 bilhão!')
                continue
            else:
                print(f'Parabéns, você depositou RS{dep}')
                saldo += dep
                saldo = round(saldo, 2)
                print(f'Seu saldo atual é: RS{saldo}')
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
                print('O saque não pose ser menor ou igual a zero!')
                continue
            elif sacar > saldo:
                print('Seu saldo é insuficiente')
                continue
            else:
                print(f'Seu saque de RS{sacar}, foi realizado com sucesso')
                saldo -= sacar
                saldo = round(saldo, 2)
                print(f'Sei saldo atual é: RS{saldo}')
            break
        continue
    elif opcao == 3:
        print('Lega! Vamos fazer um pix')

        while True:
            try:
                chave_pix = input('Chave pix: ')
            except ValueError:
                print('Chave inválido')
                continue

            if len(chave_pix) < 10:
                print('Chave inválida')
                continue

        while True:
            try:
                valor_pix = float(input('Valor do pix: RS '))
            except ValueError:
                print('Valor inválido')
                continue
            if valor_pix <+ 0 or valor_pix > 1000000000:
                print('Não é possível fazer o pix menor ou igual a zero ou maior que 1 bilhão')
                continue
            else:
                print(f'Pix de RS{valor_pix} foi realizado com sucesso')
                saldo -= valor_pix
                print(f'Seu saldo atual é: RS{saldo}')
            break
        continue
    if opcao == 4:
        print(f'Seu saldo é RS{saldo}')
        continue
    if opcao == 5:
        print('Saindo...')
        print('Programa encerrado')
    break