# Função que verifica se um número pertence à sequência de Fibonacci
def pertenceFibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def main():
    numero = int(input("Informe um número inteiro: "))
    if pertenceFibonacci(numero):
        print("O número %i pertence à sequência de Fibonacci." % numero)
    else:
        print("O número %i NÃO pertence à sequência de Fibonacci." % numero)

main()
