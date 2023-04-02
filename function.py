def fibonacci_sequence(term_1, term_2, contador):
    print('|  \033[34m', term_1, ' -> ', term_2, sep='', end='')
    for num in range(2, contador):
        term_3 = term_1 + term_2
        print(' -> ', term_3, sep='', end='')
        term_1, term_2 = term_2, term_3
    print('\033[31m -> end sequence')