# Caio Godoy - RM 98002
# Júlia Barboza - RM 98558
# Nicholas Calegari - RM 93912
# Renan Dias da Costa Silva - RM 99258
# Victor Tosto - RM 99599

# Título
print('-'*28)
print('|  Sequência de Fibonacci  |')
print('-'*28)

# Definindo a função que exibe os termos da sequência
def fibonacci_sequence(termo_1, termo_2, contador):
    # Exibindo os dois primeiros termos | parâmetro end para não pular linha
    print(f'{termo_1} -> {termo_2}', end='')

    # Para cada número na sequência de 2 até o número N
    for num in range(2, contador):
        # Definindo o terceiro termo
        term_3 = term_1 + term_2

        # Exibindo o terceiro termo
        print(f' -> {term_3}', end='')

        # Passando a sequência para frente
        term_1 = term_2
        term_2 = term_3

    # Definindo o fim da sequência
    print(' -> end sequence')
    print(' ')


# Definindo o loop infinito
while True:
    # Pulando linha
    print(' ')

    # Lendo o número inteiro N (contador)
    print('~'*52)
    n = int(input("Quantos termos você quer mostrar? "))

    # Chamando a função e passando os dois primeiros termos e N como contador
    print(' ')
    fibonacci_sequence(0, 1, n)

    # Definindo a resposta
    resp = input('Deseja continuar? (S/N): ').upper()
    if resp == 'N':
        break
