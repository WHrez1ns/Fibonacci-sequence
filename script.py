### Escreva um programa que leia um número N inteiro qualquer e
### mostre na tela os N primeiros elementos de uma Sequência de
### Fibonacci.
# EX:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

# 0 - 1 - 1 - 2 - 3
# 0+1 = 1 | 1+1 = 2 | 2+1 = 3 |

# Exibindo título
print('-'*28)
print('|  Sequência de Fibonacci  |')
print('-'*28)
print(' ')

# Lendo N
N = int(input("Quantos termos você quer mostrar? "))
# Definindo os primeiros dois termos da sequência de Fibonacci
t1 = 0
t2 = 1

# Exibindo sequência
print(' ')
# fstring para fazer referência a variáveis no código | parâmetro end para não pular linha
print(f'{t1} -> {t2}, end=''')
t3 = t1 + t2
print(f' -> {t3}, end=''')