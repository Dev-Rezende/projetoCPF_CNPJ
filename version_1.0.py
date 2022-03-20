"""
Algoritmo desenvolvido por Gustavo Caris Rezende com o objetivo de testar e aprimorar os conhecimentos na linguagem
python, onde o mesmo só deve ser utilizado para fins didáticos.
   GitHub profile: https://github.com/Dev-Rezende
   Curso: https://www.udemy.com/course/python-3-do-zero-ao-avancado/  --> Módulo 1
   Python version: 3.8
"""

# Font Color
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
resetFontColor = "\033[0;0m"

# Layout
separador = f'{cyan}\n' + (('=-' * 40) + '=') + f'\n{resetFontColor}'
separadorSecundario = '\n' + ('-' * 81) + '\n'
limpaTela = '\n' * 70

keyProgram = ''
cpf = ''
dnv = 'S'
while dnv == 'S':
    # Escolha do processo a ser executado
    print(separador)
    print(f"{yellow}SELECIONE QUAL PROGRAMA VOCÊ DESEJA EXECUTAR:\n"
          f"{blue} [0] VALIDADOR DE CPF\n"
          f" [1] GERADOR DE CPF\n{resetFontColor}")
    keyInput = True
    while keyInput:
        program = input(f"{green}Res.:{resetFontColor} ")
        if program.isnumeric():
            if program == '0':
                keyInput = False
                keyProgram = 0
            elif program == '1':
                keyProgram = 1
                keyInput = False
            else:
                print(f"{red}\nSELECIONE UM NÚMERO VÁLIDO!\n")
                continue
        else:
            print(f"{red}\nO VALOR INFORMADIO NÃO É UM NÚMERO! TENTE NOVAMENTE!\n")

    # VALIDADOR DE CPF
    if keyProgram == 0:
        # Input CPF
        cpfList = []
        cpf = ''
        keyCPF = True
        while keyCPF:
            cpf = ''
            cpfList.clear()
            cpfInput = input(f"\n{yellow}Informe o CPF: {resetFontColor}").strip()
            # Formatação
            acumulador = 0
            digRept = ''
            for iterador in cpfInput:
                if iterador == '.' or iterador == '-' or iterador == ' ':
                    continue
                else:
                    cpf += iterador
                    if iterador == digRept:
                        acumulador += 1
                digRept = iterador
                cpfList.append(iterador)
            # Pré verificação do valor digitado
            try:
                if len(cpf) != 11:
                    print(f'\n{red}VERIFIQUE O VALOR DIGITADO!{resetFontColor}')
                    continue
                else:
                    cpf = int(cpf)
                    # CPF com todos os digitos iguais são Inválidos
                    if acumulador == 10:
                        print(f"\n{red}O CPF NÃO PODE TER TODOS OS NÚMEROS IGUAIS!\nISSO O TORNA INVÁLIDO!"
                              f"{resetFontColor}\n")
                    else:
                        keyCPF = False
                        del digRept, iterador, cpfInput, acumulador
            except:
                print(f'{red}VERIFIQUE O CPF INFORMADO!{resetFontColor}\n')
        # Verificação do primeiro digito
        validaSoma, indice = 0, 0
        digV1 = int(cpfList[9])
        digV2 = int(cpfList[10])
        for iterador in range(10, 1, -1):
            validaSoma += int(cpfList[indice]) * iterador
            indice += 1
        if (validaSoma * 10) % 11 == 10:
            validaDig1 = 0
        else:
            validaDig1 = (validaSoma * 10) % 11
        if validaDig1 == digV1:
            # Verificação do segundo digito
            validaSoma, indice, iterador = 0, 0, 0
            for iterador in range(11, 1, -1):
                validaSoma += int(cpfList[indice]) * iterador
                indice += 1
            if (validaSoma * 10) % 11 == digV2:
                statusCPF = 'V'
            else:
                statusCPF = 'I'
        else:
            statusCPF = 'I'

    # GERADOR DE CPF
    elif keyProgram == 1:
        from random import randrange
        # Gera digitos
        keyNewCPF = True
        cpf = ''
        while keyNewCPF:
            cpf = ''
            for iterador in range(0, 9, 1):
                cpf = cpf + str(randrange(0, 9))
            checkCPF = ''
            digitosIguais = 0
            for iterador in cpf:
                if iterador == checkCPF:
                    digitosIguais += 1
                checkCPF = iterador
            if digitosIguais == 8:
                continue
            else:
                keyNewCPF = False
        # Geração do primeiro digito de verificação
        veriDig1 = 0
        indice = 0
        for iterador in range(10, 1, -1):
            veriDig1 = (int(cpf[indice]) * iterador) + veriDig1
            indice += 1
        veriDig1 = (veriDig1 * 10) % 11
        if veriDig1 == 10:
            veriDig1 = 0
        cpf += str(veriDig1)
        # Geração do segundo digito de validação
        veriDig2 = 0
        indice = 0
        for iterador in range(11, 1, -1):
            veriDig2 = (int(cpf[indice]) * iterador) + veriDig2
            indice += 1
        veriDig2 = (veriDig2 * 10) % 11
        if veriDig2 == 10:
            veriDig2 = 0
        cpf += str(veriDig2)

    # Formatando o CPF
    cpf = str(cpf)
    cpfFormatado = ''
    for iterador in range(0, 11, 1):
        if iterador == 3 or iterador == 6:
            cpfFormatado += '.'
        elif iterador == 9:
            cpfFormatado += '-'
        cpfFormatado += cpf[iterador]

    # Output:
    if program == '0':
        # Output Validador
        print(separador)
        if statusCPF == 'I':
            print(f"{red}O CPF {cpfFormatado} É INVÁLIDO!{resetFontColor}")
        elif statusCPF == 'V':
            print(f"{green}O CPF {cpfFormatado} É VÁLIDO!{resetFontColor}")
        # ERRO ST4T1S:
        else:
            print("\nOPS! ALGO DEU ERRADO, ENTRE EM CONTATO!\nCÓDIGO ERRO: ST4T1S!")
    elif program == '1':
        # Output Gerador
        print(separador)
        print(f"{yellow}CPF GERADO: {green}{cpfFormatado}{resetFontColor}")
    # Erro: 0UTPUTR3S
    else:
        print("\nOPS1 ALGO DEU ERRADO! CÓDIGO ERRO: 0UTPUTR3S\n")

    # Executar novamente
    keyDNV = True
    while keyDNV:
        print(separador)
        dnv = input(f"{yellow}Deseja executar o programa novamente [S/N]: {resetFontColor}").upper()
        if dnv == 'S' or dnv == 'N':
            keyDNV = False
        else:
            print(f"{red}\nVALOR DIGITADO INVÁLIDO!{resetFontColor}")

# Encerramento do programa
print(separador)
