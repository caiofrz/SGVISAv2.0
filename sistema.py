from estabelecimentos import Estabelecimento
from ListaEstab import ListaEstab
from funcionarios import Funcionario
from VISA.lib.interface import *
from VISA.lib.arquivo import *
from time import sleep
from visita import Visita
from ListaVisita import ListaVisita
from datetime import date

print("\t  \033[32:40mSistema Gerenciador da Visa v2.0\33[m")

arqfuncionario = 'VisaFuncionario.txt'
arqestabelecimento = 'VisaEstabelecimento.txt'
arqvisita = 'VisaVisita.txt'

funcionario = ListaFunc()
estabelecimento = ListaEstab()
visita = ListaVisita()


if not arquivoExiste(arqfuncionario):
    criarArquivo(arqfuncionario)

if not arquivoExiste(arqestabelecimento):
    criarArquivo(arqestabelecimento)

if not arquivoExiste(arqvisita):
    criarArquivo(arqvisita)


def main_func():
    with open(arqfuncionario, 'r', encoding="UTF-8") as arquivo:
        for v in arquivo:
            dados = v.replace('\n', '').split("\t")
            func = Funcionario(dados[0], dados[1], dados[2], dados[3])
            funcionario.inserir(func, func.cpf)


def main_estb():
    with open(arqestabelecimento, 'r', encoding="UTF-8") as arquivo:
        for v in arquivo:
            dado = v.replace('\n', '').split("\t")
            estab = Estabelecimento(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5])
            estabelecimento.inserir(estab, estab.cnpj)


def main_visita():
    with open(arqvisita, 'r', encoding="UTF-8") as arquivo:
        for v in arquivo:
            dad = v.replace('\n', '').split("\t")
            vis = Visita(dad[0], dad[1], dad[2])
            visita.inserir(vis, vis.cnpj)


main_func()
main_estb()
main_visita()


def cadastra_visita():
    razão_social = input('RAZÃO SOCIAL: ')
    cnpj = input('CNPJ: ')
    while True:
        dia = leiaInt('DIA: ')
        if dia > 31 or dia < 0:
            print('\033[0;31mERRO! Digite um dia válido.\033[m')
        else:
            break
    while True:
        mes = leiaInt('MÊS: ')
        if mes > 12 or mes < 0:
            print('\033[0;31mERRO! Digite o mês válido.\033[m')
        else:
            break
    while True:
        ano = leiaInt('ANO: ')
        if ano > 2050 or ano < 2022:
            print('\033[0;31mERRO! Digite o ano válido.\033[m')
        else:
            break
    data = date(ano, mes, dia)
    nova_visita = Visita(razão_social, cnpj, data)
    visita.inserir(nova_visita, cnpj)


def cadastra_funcionario():
    nome = input('NOME: ')
    cpf = input('CPF: ')
    telefone = input('TELEFONE: ')
    funcao = input('FUNÇÃO: ')

    novo_funcionario = Funcionario(nome, cpf, telefone, funcao)
    funcionario.inserir(novo_funcionario, cpf)


def cadastra_estabelecimentos():
    razao_social = input('RAZÃO SOCIAL: ')
    CNPJ = input('CNPJ: ')
    telefone = input('TELEFONE: ')
    atividade_economica = input('CNAE: ')
    print('Data de vencimento do alvará santário:')
    sleep(1)
    while True:
        dia = leiaInt('DIA: ')
        if dia < 31 and dia > 0:
            break
        else:
            print('\033[0;31mERRO! Digite um dia válido.\033[m')
    while True:
        mes = leiaInt('MÊS: ')
        if mes < 12 and mes > 0:
            break

        else:
            print('\033[0;31mERRO! Digite o mês válido.\033[m')
    while True:
        ano = leiaInt('ANO: ')
        if ano < 2050 and ano > 2021:
            break
        else:
            print('\033[0;31mERRO! Digite o ano válido.\033[m')
    data_validade_alvara = date(ano, mes, dia)

    print('SITUAÇÃO DO ESTABELECIMENTO: ')
    situacao = leiaInt('\t[1]: Aguarda cumprimento de ressalvas para Alvará Inicial\n'
                       '\t[2]: Interdição cautelar\n'
                       '\t[3]: Não protocolou situação de renovação de Alvará\n'
                       '\t[4]: Alvará vigente e dentro do prazo para solicitação de renovação \n'
                       '\t[5]: Alvará vencido e estabelecimento não cumpriu ressalvas apontadas no Relatório de '
                       'Inspeção\n '
                       '\t[6]: Atividade não sujeita a concessão de Alvará Sanitário\n'
                       '\t[7]: Alvará vencido, protocolou solicitação de renovação e aguarda inspeção\n'
                       'Escolha uma opção: ')

    novo_estabelecimento = Estabelecimento(razao_social, CNPJ, telefone, atividade_economica, data_validade_alvara,
                                           situacao)
    estabelecimento.inserir(novo_estabelecimento,CNPJ)


while True:
    cabecalho('MENU PRINCIPAL')
    resposta = menu(['Estabelecimentos', 'Funcionario', 'Fechar o Programa'])
    sleep(0.5)
    if resposta == 1:
        while True:
            cabecalho('ESTABELECIMENTOS')
            resp1 = menu(['Cadastra novo estabelecimentos', 'Listar estabelecimentos',
                          'Remover Estabelecimento', 'Visita','Situação', 'Voltar ao menu anterior'])
            sleep(0.5)

            if resp1 == 1:
                cabecalho('NOVO CADASTRO')
                cadastra_estabelecimentos()
                estabelecimento.arq_estab()
                print('-' * 47)
                print('\033[32m     Estabelecimento cadastrado com sucesso!\033[m')
                print('-' * 47)
                sleep(0.5)

            elif resp1 == 2:
                cabecalho('LISTA DE ESTABELECIMENTOS')
                print('----Razão Social---------------CNPJ-----------Telefone--------CNAE------VL. Alvará--ST')

                estabelecimento.printERD()
                print('-'*86)

            elif resp1 == 3:
                print('----Razão Social---------------CNPJ-----------Telefone--------CNAE------VL. Alvará--ST')
                estabelecimento.printERD()
                print('-'*86)
                valor = input('\033[33mInforme o CNPJ do estabelecimento que você deseja remover? \033[m')
                estabelecimento.excluir(valor)
                print()

            elif resp1 == 4:
                cabecalho('VISITA')
                while True:
                    resp = menu(['Agendar Visita', 'Listar Visitas', 'Remover Visita', 'Voltar ao menu anterior'])
                    if resp == 1:
                        cabecalho('AGENDAR VISITA')
                        cadastra_visita()
                        print('-' * 42)
                        print('\033[32m     Visita Agendada com sucesso!\033[m')
                        print('-'*42)
                        sleep(0.5)
                    elif resp == 2:
                        cabecalho('LISTAR VISITAS')
                        print('----Razão Social-----------CNPJ------------DATA---')
                        visita.printERD()
                        print('-'*50)
                        sleep(0.5)
                    elif resp == 3:
                        cabecalho('REMOVER VISITAS')
                        print('----Razão Social-----------CNPJ------------DATA---')
                        visita.printERD()
                        print('--------------------------------------------------')
                        valor = input('\033[33mInforme o CNPJ do estabalecimento que deseja remover a visita: \033[m')
                        visita.excluir(valor)
                        print('-'*65)
                        sleep(0.5)
                    elif resp == 4:
                        break
                    else:
                        print('\033[31mERR0! Digite uma opção válida!\033[m')

            elif resp1 == 5:
                cabecalho('SITUAÇÃO')
                sit = input('\033[33mInforme o CNPJ para verifiar a Situação do estabelecimento: \033[m')
                estabelecimento.situacao(sit)
            elif resp1 == 6:
                break
            else:
                print('\033[31mERR0! Digite uma opção válida!\033[m')
        print()

    elif resposta == 2:
        while True:
            cabecalho('FUNCIONÁRIOS')
            resp2 = menu(['Cadastra novo funcionário', 'Listar funcionários', 'Remover Funcionários',
                          'Voltar ao menu anterior'])
            sleep(0.5)

            if resp2 == 1:
                cabecalho('NOVO CADASTRO')
                cadastra_funcionario()
                print('\033[33mNovo registro foi adicionado.\033[m')
                sleep(0.5)

            elif resp2 == 2:
                cabecalho('LISTA DE FUNCIONÁRIOS')
                print('-------NOME--------------CPF-----------TELEFONE-----FUNÇÃO-')
                funcionario.printERD()
                print('-' * 59)


            elif resp2 == 3:
                cabecalho('REMOVER FUNCIONÁRIOS')
                funcionario.printERD()
                print('-' * 59)
                cpf = input('\033[33mInforme o CPF do funcionário que deseja remover: \033[m')
                funcionario.excluir(cpf)

            elif resp2 == 4:
                break
            else:
                print('\033[31mERR0! Digite uma opção válida!\033[m')
            print()

    elif resposta == 3:
        estabelecimento.arq_estab()
        funcionario.arq()
        visita.arq()
        contagem('Saindo do sistema')
        print('\033[33m\nAté logo! \033[m')
        break
    else:
        print('\033[31mERR0! Digite uma opção válida!\033[m')
