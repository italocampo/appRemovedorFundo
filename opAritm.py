# Operações Matemáticas

x, y, z, w, t, s =  15, -10, 0.8, 0, 9, 5.6

soma = x + t       # Adição
sub = x - t        # Subtração
mul = x * y        # Multiplicação
div = x / y        # Divisão real (resultado float)
quo = x // t       # Divisão inteira (correto, em vez de int(x/t))
resto = x % y      # Módulo (resto da divisão)
pot = x ** y       # Potência
raiz = t ** 0.5    # Raiz quadrada (ou raiz cúbica = t ** (1/3))


# print(soma)
# print(sub)
# print(mul)
# print(raiz)
# print(div)
# print(quo)
# print(resto)
# print(pot)

# Operações matemáticas com funções padrão do python

print(abs(-10))              # Valor absoluto
print(pow(5,3))              # Potência (equivalente a 5 ** 3)
print(round(3.14253, 2))     # Arredondamento com 2 casas decimais
print(max(5,6,9,6.3))        # Maior valor da lista
print(min(7.2, 2.2, 10))     # Menor valor da lista
print(sum([1,2,3,4,5]))      # Soma dos elementos da lista
print(divmod(10, 3))         # Retorna (quociente, resto)

# Aplicação prática dop SUM e LEN

notas = [6.8, 7.7, 5.9, 10, 0]
media = sum(notas) / len(notas)
# print(media)

# Aplicação prática do DIVMOD

# prod = 153
# qtd_garrafa_pct = 6
# dados = divmod(prod, qtd_garrafa_pct)
# print(f"Produzido {dados[0]} fardos, restando {dados[1]} garrafas.")

# Operações matemáticas avançada com biblioteca math
import math

print(math.sqrt(25))     # Raiz quadrada
print(math.pow(5,3))     # Potência
print(math.pi)           # Constante Pi
print(math.e)            # Constante de Euler
print(math.ceil(3.156))  # Arredonda para cima
print(math.floor(3.156)) # Arredonda para baixo
print(math.trunc(3.156)) # Trunca (corta a parte decimal)
print(math.factorial(5)) # Fatorial
print(math.gcd(12, 18))  # Máximo divisor comum (MDC)
print(math.log(1000, 10)) # Logaritmo base 10
print(math.log10(1000))   # Logaritmo base 10
print(math.log2(1024))    # Logaritmo base 2

# Funções trigonométricas
print(math.sin(math.radians(45))) # Seno
print(math.cos(math.radians(45))) # Cosseno
print(math.tan(math.radians(45))) # Tangente
print(math.asin(1))  # Arco seno
print(math.acos(1))  # Arco cosseno


# Operação matemáticas com método random

import random

print(random.randint(0, 10))  # Número inteiro aleatório entre 0 e 10
print(random.uniform(0, 10))  # Número float entre 0 e 10
print(random.random())        # Número float entre 0 e 1
print(random.randrange(0, 10, 2))  # Número par entre 0 e 10
print(random.choice(['Italo', 'Cinthia', 'Junior', 'Rony', 'Marcelo'])) # Escolhe 1 aleatório
print(random.choices(['Italo', 'Cinthia', 'Junior', 'Rony', 'Marcelo'], k=2)) # Escolhe 2 aleatórios


# Operações matemáticas complexas com Numpy
import numpy as np

dados = [10, 2, 3, 41, 5]

print(np.mean(dados))   # Média
print(np.median(dados)) # Mediana
print(np.std(dados))    # Desvio padrão
print(np.var(dados))    # Variância
print(np.sum(dados))    # Soma
print(np.prod(dados))   # Produto dos elementos

