import operacoes
import utils

operacao = input("Escolha a operação (+, -, *, /): ")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = operacoes.soma(a, b)
elif operacao == '-':
    resultado = operacoes.subtracao(a, b)
elif operacao == '*':
    resultado = operacoes.multiplicacao(a, b)
elif operacao == '/':
    resultado = operacoes.divisao(a, b)
else:
    resultado = "Operação inválida."

utils.exibir_resultado(operacao, resultado)
