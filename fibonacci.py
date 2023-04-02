# Caio Godoy - RM 98002
# Júlia Barboza - RM 98558
# Nicholas Calegari - RM 93912
# Renan Dias da Costa Silva - RM 99258
# Victor Tosto - RM 99599

print('\033[32m-'*28)
print('|  Sequência de Fibonacci  |')
print('-'*28)

def fibonacci_sequence(term_1, term_2, contador):
    print(f'\033[34m{term_1} -> {term_2}', end='')
    for num in range(2, contador):
        term_3 = term_1 + term_2
        print(f' -> {term_3}', end='')
        term_1 = term_2
        term_2 = term_3
    print('\033[31m -> end sequence')
    print(' ')

while True:
    print(' ')
    print('\033[32m~'*104)
    print(' ')
    while True:
        try:
            n = int(
                input('\033[37mQuantos termos você quer mostrar? \033[35m'))
            if n < 2:
                print('\033[31m*ERROR* O número precisa ser maior do que 2!')
            else:
                break
        except:
            print('\033[31m*ERROR* Apenas números são válidos!')
    print(' ')
    fibonacci_sequence(0, 1, n)
    resp = input(
        '\033[37mDeseja continuar? \033[33m(S/N): \033[35m').upper()
    if resp == 'N' or resp != 'S':
        break
