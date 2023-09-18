# REVISÃO DAS ESTRUTURAS BÁSICAS EM PYTHON

# -----------------------------------------------------------
# Tipos de dados

# int (inteiros)
a = 30
b = -50
c = 0

# float (números reais)
a = 40.5
b = -3.99
c = 3.0

# str (strings / texto)
a = 'Paulo'
b = "Exemplo de texto!!"

# bool (valores lógicos)
a = True
b = False

# função type (verifica o tipo de dado)
a = 4.5
print(type(a))
if type(a) != float:
    print('É um float')

# funções de conversão de tipo
a = '3.99'
a = float(a)    # converte para float
print(a)

a = 2.85
a = int(a)      # converte para int
print(a)

a = 2.85
a = str(a)      # converte para string
print(a)


# -----------------------------------------------------------
# Operadores Aritméticos
print(2 + 2)        # adição
print(2 - 2)        # subtração
print(2 * 3)        # multiplicação
print(10 / 3)       # divisão
print(10 // 3)      # divisão inteira
print(10 % 3)       # resto da divisão (mod / modulo)
print(2 ** 5)       # potência

# prioridades das operações
# 1º: **
# 2º: * / // %
# 3º: + -

# Operadores Relacionais
print(2 == 3)       # igualdade
print(2 != 3)       # diferente
print(2 < 3)        # menor
print(2 > 3)        # maior
print(2 <= 3)       # menor ou igual
print(2 >= 2)       # maior ou igual

# Operadores Lógicos
print(2 == 2 and 2 == 3)    # E
print(2 == 2 or 2 == 3)     # OU
print(not 2 == 2)           # NÃO


# -----------------------------------------------------------
# operações de entrada (input)

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Diigte a sua altura: '))


# -----------------------------------------------------------
# operações de saída (print)
nome = 'Paulo'
idade = 30
print(nome, idade)
print('O seu nome é', nome, 'e sua idade é', idade, 'anos')
print('O seu nome é {} e sua idade é {} anos'.format(nome, idade))
print(f'O seu nome é {nome} e sua idade é {idade} anos')        # f-string (forma atual)


# -----------------------------------------------------------
# Estrutas condicionais (if elif else)

# verifica se o número é par ou ímpar
numero = int(input('Digite um número: '))
if numero % 2 == 0:             # True
    print('O número é par')
else:                           # False
    print('O número é ímpar')

# verifica se o número é positivo ou negativo ou zero
if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
else:
    print('O número é igual a zero')


# -----------------------------------------------------------
# estrutura de seleção (match/case)
numero = int(input('Informe um número: '))
match numero:
    case 1: 
        print('O número é igual a um')
    case 2:
        print('O número é igual a dois')
    case 3 | 4:     # operação or
        print('O número é igual a três ou quatro')
    case _:         # default
        print('É um outro número')


# -----------------------------------------------------------
# estrutura de repetição while

# validação de uma senha
senha_correta = '123'
senha = input('Digite a senha: ')
while senha != senha_correta:
    print('Senha Incorreta. Tente novamente.')
    senha = input('Digite a senha: ')
print('Você acertou a senha...')

# exibir os numeros inteiros de 1 a 5
cont = 1
while cont <= 5:
    print(cont)
    cont += 1

# solicitar 5 números para o usuário e calcular o somatório dos numeros
soma = 0
cont = 1
while cont <= 5:
    numero = int(input('Número: '))
    soma += numero          # somadora
    cont += 1               # contadora
print(f'Somatório dos números: {soma}')


# -----------------------------------------------------------
# Estrutura de repetição for

# exibir os numeros inteiros de 1 a 5
for a in range(1, 6):
    print(a)

# solicitar 5 números para o usuário e calcular o somatório dos numeros
soma = 0
for a in range(5):
    numero = int(input('Numero: '))
    soma += numero
print(f'Somatório dos números: {soma}')


# -----------------------------------------------------------
# Funções

# definição da função
def somar(a, b):
    c = a + b
    return c

c = somar(3, 7)
print(f'Resultado da soma: {c}')

x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))
print(f'Resultado da soma: {somar(x, y)}')
