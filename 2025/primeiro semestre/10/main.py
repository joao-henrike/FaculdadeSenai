from modulos.operacoes import soma, subtracao, multiplicacao, divisao
from modulos.utils import exibir_resultado

def main():
    operacao = input("Escolha uma operação (+, -, *, /): ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = soma(a, b)
        exibir_resultado("soma", resultado)
    elif operacao == '-':
        resultado = subtracao(a, b)
        exibir_resultado("subtração", resultado)
    elif operacao == '*':
        resultado = multiplicacao(a, b)
        exibir_resultado("multiplicação", resultado)
    elif operacao == '/':
        resultado = divisao(a, b)
        exibir_resultado("divisão", resultado)
    else:
        print("Operação inválida.")

if __name__ == "__main__":
    main()
