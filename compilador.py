# -*- coding: utf-8 -*-
import sys
import traceback
sys.stdout.reconfigure(encoding='utf-8')


def analisador_lexico(expressao):
    """Faz análise dos caracteres."""
    tokens = []
    i = 0
    while i < len(expressao):
        if digito(expressao[i]):
            j = i
            while j < len(expressao) and (digito(
                    expressao[j]) or expressao[j] == '.'):
                j += 1
            tokens.append(expressao[i:j])
            i = j
        elif expressao[i] in ('+', '-', '*', '/'):
            tokens.append(expressao[i])
            i += 1
        elif expressao[i] in ('(', ')'):
            tokens.append(expressao[i])
            i += 1
        else:
            raise Exception('Erro léxico, caractere inválido encontrado')

    return tokens


def analisador_sintatico(tokens):
    """Faz uma analise sobre a sintaxe da expressao."""
    pilha_num = []
    pilha_op = []
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if digito(token) or digito(token.replace('.', '', 1)):
            pilha_num.append(float(token))
        elif token in precedencia:
            while pilha_op and precedencia.get(
                    pilha_op[-1], 0) >= precedencia[token]:
                op = pilha_op.pop()
                num2 = pilha_num.pop()
                num1 = pilha_num.pop()
                if op == '+':
                    pilha_num.append(num1 + num2)
                elif op == '-':
                    pilha_num.append(num1 - num2)
                elif op == '*':
                    pilha_num.append(num1 * num2)
                elif op == '/':
                    pilha_num.append(num1 / num2)
            pilha_op.append(token)
        elif token == '(':
            pilha_op.append(token)
        elif token == ')':
            while pilha_op[-1] != '(':
                op = pilha_op.pop()
                num2 = pilha_num.pop()
                num1 = pilha_num.pop()
                if op == '+':
                    pilha_num.append(num1 + num2)
                elif op == '-':
                    pilha_num.append(num1 - num2)
                elif op == '*':
                    pilha_num.append(num1 * num2)
                elif op == '/':
                    pilha_num.append(num1 / num2)
            pilha_op.pop()

    while pilha_op:
        op = pilha_op.pop()
        num2 = pilha_num.pop()
        num1 = pilha_num.pop()
        if op == '+':
            pilha_num.append(num1 + num2)
        elif op == '-':
            pilha_num.append(num1 - num2)
        elif op == '*':
            pilha_num.append(num1 * num2)
        elif op == '/':
            pilha_num.append(num1 / num2)
    return pilha_num[0]


def digito(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def analisador_semantico(expressao):
    operadores = set(['+', '-', '*', '/'])
    count_parenteses = 0
    for i in range(len(expressao)):
        if expressao[i] == '(':
            count_parenteses += 1
            # Verificamos se abertura de parenteses vem depois de um operador,
            # Exceto caso a expressao comece por um parenteses.
            if i > 1 and not expressao[i - 1] in operadores:
                raise Exception('Erro de semântica')
            # verificamos se apos a abertura do parenteses tem eh diferente de
            # um numero e diferente de outro parenteses
            elif not digito(expressao[i + 1]) and expressao[i + 1] != '(':
                raise Exception('Erro de semântica')
        elif expressao[i] == ')':
            count_parenteses -= 1
            # Antes do parenteses fechado tem que ser um digito
            # ou outro parenteses fechado
            if i > 1 and not digito(expressao[i - 1]) and expressao[
                    i - 1] != ')':
                raise Exception('Erro de semântica')
            elif i < len(expressao) - 1: 
                if not expressao[i + 1] in operadores and expressao[
                        i + 1] != ')':
                    raise Exception('Erro de semântica')
        # Verificamos se existe sequencia de 2 operadores
        elif expressao[i] in operadores:
            if i > 1 and (expressao[i - 1] in operadores or expressao[
                    i + 1] in operadores):
                raise Exception(
                    '2 ou mais operadores consecutivos na expressão.')
    # Se existir parentes nao fechados, gera erro
    if count_parenteses != 0:
        raise Exception('Erro na abertura ou fechamento dos parênteses')
    return


indice_exp = 0
debug = True
linha = ''

while True:
    try:
        texto = input().strip().replace(' ', '')
        if not texto:
            break
        linha += texto
    except EOFError:
        break

try:
    expressoes = linha.split(';')
    expressoes_tratadas = list(filter(bool, expressoes))
    # raise Exception(expressoes_tratadas)
    for indice, exp in enumerate(expressoes_tratadas):
        indice_exp += 1
        analisador_semantico(exp)
        exp_tokens = analisador_lexico(exp)
        resultado = analisador_sintatico(exp_tokens)
        print(resultado)
except Exception as e:
    tb = traceback.extract_tb(sys.exc_info()[2])[-1]

    msg = 'Erro: %s \n%sº Expressão' % (e, indice_exp)
    if debug:
        msg += '\nDebug: Linha %s: %s' % (tb.lineno, tb.line)
    print(msg)
