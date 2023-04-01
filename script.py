# Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de
# Fibonacci.
# EX:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

# 0 - 1 - 1 - 2 - 3
# 0+1 = 1 | 1+1 = 2 | 2+1 = 3 |

# Exibindo título
print('-'*28)
print('|  Sequência de Fibonacci  |')
print('-'*28)
print(' ')

# Definindo os termos iniciais
t1 = 0
t2 = 1
contador = 3
resp = 'S'

def sdf(t1, t2, contador):
    # Lendo N
    N = int(input("Quantos termos você quer mostrar? "))

    # Exibindo sequência
    print(' ')
    # fstring para fazer referência a variáveis no código | parâmetro end para não pular linha
    print(f'{t1} -> {t2}', end='')

    while contador <= N:
        t3 = t1 + t2
        print(f' -> {t3}', end='')
        # jogando os termos t1 e t2 para frente
        t1 = t2
        t2 = t3

        # Adicionando 1 ao contador para chegar até o valor definido "N"
        contador += 1

while True:
    sdf(t1, t2, contador)
    print(' -> end sequence')
    print(' ')
    t1 = 0
    t2 = 1
    contador = 3
    while (resp == 'S'):
        print('Deseja continuar?')
        resp = input('Digite S ou N: ').upper()
        if (resp == 'N'):
            exit()
        else:
            print(' ')
            sdf(t1, t2, contador)
            print(' -> end sequence')
            print(' ')

