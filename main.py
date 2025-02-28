from minhasoperacoes import operacoes
from minhasoperacoes import utils

# Escolher uma operação
EsqOperacao = input('Escolha uma operação (+, -, *, /): ')

# Pedir dois números
a = float(input('Insira um número: '))
b = float(input('Insira outro número: '))

# Execute a operação correspondente e exiba o resultado
if EsqOperacao == '+':
    resultado = operacoes.soma(a, b)
    print(utils.exibir_resultado("soma", resultado))

elif EsqOperacao == '-':
    resultado = operacoes.subtracao(a, b)
    print(utils.exibir_resultado("subtração", resultado))

elif EsqOperacao == '*':
    resultado = operacoes.multiplicacao(a, b)
    print(utils.exibir_resultado("multiplicação", resultado))

elif EsqOperacao == '/':
    resultado = operacoes.divisao(a, b)
    print(utils.exibir_resultado("divisão", resultado))

else:
    print("Operação inválida! Escolha entre +, -, * ou /.")
