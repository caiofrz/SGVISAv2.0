def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        else:
            valido = True
            return float(entrada)


def linha (tam=21):
    return '=-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m = \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


def contagem(txt):
    from time import sleep
    l = ['.', '.', '.', '.']
    print(f'\033[36m{txt} \033[m', end='')
    for x in l:
        print(f'\033[36m{x}\033[m', end=' ', flush=True)
        sleep(0.5)