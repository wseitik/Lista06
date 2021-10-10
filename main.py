# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv

import pytest

teste_dados_tabuada = [
    (1, 40),
    (2, 80),
    (3, 120),
    (4, 160),
    (-5, 200)
]

@pytest.mark.parametrize('numero,resultado', teste_dados_tabuada)
def testar_tabuada_lista(numero, resultado):
    assert calcular_fosforos(numero) == resultado


@pytest.mark.parametrize('numero,resultado', teste_dados_tabuada)
def testar_valor_negativo(numero, resultado):
    if calcular_fosforos(numero) < 0:
        return print(f'O número informado: {numero} é negativo')
    else:
        return print(f'O número informado: {numero} é positivo')

def ler_dados_csv():
    teste_csv = []
    nome_arquivo = 'Tabuada.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                teste_csv.append(linha)
        return teste_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrada: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


@pytest.mark.parametrize('numero,resultado', ler_dados_csv())
def testar_dados_csv(numero, resultado):
    assert calcular_fosforos(int(numero)) == int(resultado)


@pytest.mark.parametrize('numero,resultado', ler_dados_csv())
def testar_valor_diferente_zero_csv(numero, resultado):
    assert calcular_fosforos(int(resultado)) != 0

# Função Calcular fosforo

def calcular_fosforos(numero1):
    return numero1 * 40


# Unit tests - Fosforos

def test_calcular_fosforos():
    # 1 - Configurar / Preparar
    numero1 = 2  # input
    resultado_esperado = 80  # output

    # 2 - Executar
    resultado_atual = calcular_fosforos(numero1)

    # 3 Validação
    assert resultado_atual == resultado_esperado


def test_multiplicar_fosforos():
    assert calcular_fosforos(3) == 120


def test_multiplicar_fosforos_negativo():
    assert calcular_fosforos(3) == -120


# Função Tabuada

def tabuada1(num2):
    print('{} x {} = {}'.format(num2, 1, num2 * 1))
    print('{} x {} = {}'.format(num2, 2, num2 * 2))
    print('{} x {} = {}'.format(num2, 3, num2 * 3))
    print('{} x {} = {}'.format(num2, 4, num2 * 4))
    print('{} x {} = {}'.format(num2, 5, num2 * 5))
    print('{} x {} = {}'.format(num2, 6, num2 * 6))
    print('{} x {} = {}'.format(num2, 7, num2 * 7))
    print('{} x {} = {}'.format(num2, 8, num2 * 8))
    print('{} x {} = {}'.format(num2, 9, num2 * 9))
    print('{} x {} = {}'.format(num2, 10, num2 * 10))
    return (num2)


# Unit test tabuada
def test_tabuada():
    num2 = 8
    resultado_esperado = 32
    resultado_atual = tabuada1(num2) * 4
    assert resultado_atual == resultado_esperado


def tabuada(num):
    for i in range(1, 11):
        print(num, 'x', i, '=', num * i)


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    resultado = calcular_fosforos(2)
    print(f'A contagem de fósforos é de: {resultado}')

    print('Tabuada')

    num2 = int(input('Digite um número para calcular a tabuada: '))
    print(tabuada1(num2))

    num = int(input('Digite um número para calcular a tabuada: '))
    print(tabuada(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
