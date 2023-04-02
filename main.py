'''
Caio Godoy - RM 98002
Júlia Barboza - RM 98558
Nicholas Calegari - RM 93912
Renan Dias da Costa Silva - RM 99258
Victor Tosto - RM 99599
'''

from function import fibonacci_sequence
import time

print('\033[32m' + '-' * 28)
print('|  Sequência de Fibonacci  |')
print('-' * 28 + '')
print('|  ')

while True:
    print('\033[0m-' * 108 + '')
    while True:
        try:
            n = int(
                input('\033[37m|  Quantos termos você quer mostrar? \033[35m'))
            if n < 2:
                print('\033[31m|  *ERROR* O número precisa ser maior do que 2!')
            else:
                break
        except ValueError:
            print('\033[31m|  *ERROR* Apenas números são válidos!')

    print('\033[0m-' * 108 + '')
    fibonacci_sequence(0, 1, n)
    print('\033[0m|  ')

    while True:
        resp = input(
            '\033[37m|  Deseja continuar? \033[33m(S/N): \033[35m').upper()
        if resp in ('S', 'N'):
            break
        print('\033[31m|  *ERROR* Digite S ou N!')

    if resp == 'S':
        print('\033[0m|  ')
        print('|  \033[35mContinuando!')
    else:
        print('\033[0m|  ')
        print('|  \033[35mEncerrando...')
        time.sleep(1)
        break
