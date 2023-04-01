<a href="https://www.fiap.com.br/">
<img src="fiap.png" width="140" height="50">
</a> <br>


<a href="https://www.instagram.com/fiapoficial/">
<img src="ig.png">
</a>

<a href="https://www.youtube.com/@FiapBrasil">
<img src="yt.png">
</a>

# Fibonacci-sequence

<h2> Checkpoint 24/03/2023 - <a href="https://www.linkedin.com/in/fabio-cabrini/"> Fábio Henrique Cabrini </a></h2>
  
  <h3>Objetivo:</h3>
  Elaborar um programa em linguagem <a href="https://www.python.org/"> {c:green}Python{/c} </a>que leia um número inteiro N e, em seguida, mostre na tela os N primeiros termos da sequência de Fibonacci. O valor de N sendo no mínimo 2.
  
  * Editor Utilizado: <a href="https://code.visualstudio.com/"> Visual Studio Code</a>.
  
  <h3>Explicação do código:</h3>
  
  Esse código é um programa em Python que exibe os termos da sequência de Fibonacci.

Primeiro, o programa exibe um título em verde e traços decorativos. Em seguida, é definida uma função chamada fibonacci_sequence que recebe três parâmetros: term_1, term_2 e contador.

```
print('\033[32m-'*28)
print('|  Sequência de Fibonacci  |')
print('-'*28)

def fibonacci_sequence(term_1, term_2, contador):
```

Dentro da função, os dois primeiros termos são exibidos em azul, seguidos pelos próximos termos da sequência até o número contador. Em cada iteração do loop for, o terceiro termo é calculado e exibido em azul, e em seguida, a sequência é passada para frente. Ao final da exibição dos termos, é exibida a mensagem "end sequence" em vermelho.

```
def fibonacci_sequence(term_1, term_2, contador):
    print(f'\033[34m{term_1} -> {term_2}', end='')
    for num in range(2, contador):
        term_3 = term_1 + term_2
        print(f' -> {term_3}', end='')
        term_1 = term_2
        term_2 = term_3
    print('\033[31m -> end sequence')
    print(' ')
```

Em seguida, o programa entra em um loop infinito que permite que o usuário escolha quantos termos da sequência de Fibonacci deseja ver. O usuário é solicitado a inserir um número inteiro. Se o usuário inserir algo que não seja um número inteiro, uma mensagem de erro em vermelho é exibida e ele é solicitado a inserir um número inteiro novamente.

```
while True:
    print(' ')
    print('\033[32m~'*104)
    print(' ')
    while True:
        try:
            n = int(
                input('\033[37mQuantos termos você quer mostrar? \033[35m'))
            break
        except:
            print('\033[31m*ERROR* Apenas números são válidos!')
    print(' ')
    fibonacci_sequence(0, 1, n)
```

Após a exibição dos termos, o usuário é perguntado se deseja continuar a exibir a sequência. Se a resposta for "N" ou qualquer outra resposta diferente de "S", o loop infinito é interrompido e o programa é finalizado.

```
resp = input('\033[37mDeseja continuar? \033[33m(S/N): \033[35m').upper()
if resp == 'N' or resp != 'S':
    break
```

**<h3>Colaboradores:</h3>**

<a href="https://github.com/CazedaFIAP"> Caio Godoy</a>, <a href="https://github.com/Aykie"> Júlia Barboza Brunelli</a>, <a href="https://github.com/NCalegariS"> Nicholas Calegari</a>, <a href="https://github.com/WHrez1ns"> Renan Dias</a> e <a href=""> Victor Tosto</a>
<br>
**RM: 98002, 98558, 93912, 99258 e 99599.**



