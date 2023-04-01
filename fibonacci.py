print('-'*28)
print('|  Sequência de Fibonacci  |')
print('-'*28)


def fibonacci_sequence(t1, t2, n):
    print(f'{t1} -> {t2}', end='')

    for i in range(2, n):
        t3 = t1 + t2
        print(f' -> {t3}', end='')

        t1 = t2
        t2 = t3

    print(' -> end sequence')
    print(' ')


while True:
    print(' ')
    print('~'*52)
    n = int(input("Quantos termos você quer mostrar? "))

    print(' ')
    fibonacci_sequence(0, 1, n)

    resp = input('Deseja continuar? (S/N): ').upper()
    if resp == 'N':
        break
