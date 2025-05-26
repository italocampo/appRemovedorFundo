#Operadores Booleanos e Binários

#AND  OR NOT
x = 'a' #97 em decimal       #Dica: 'a' para o 'A' é -32 e do 'A' para o 'a' é +32
y = 'b' #98 em decimal

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

z = 10
w = 5
# print((z >= w) and (z > w)) # O V se baseia na primeira condição
# print((z >= w) or (z > w)) 
# print((z >= w) and not (z > w)) 
# print(not((z >= w) and not(z > w)))

#Operadores de atribuição e identidade

a = 10
a+= 5 # a = a + 5
# print(a)
a -= 2 # a = a - 2
# print(a)
a *= 2 # a = a * 2
# print(a)

nome = "python"
# print('p' in nome)
# print('P' not in nome)

linguagem = nome
# print(linguagem)
# print(linguagem is nome)
# print(linguagem is not nome)
nome = 'Java'
# print(nome)
# print(linguagem)

#Entrada de dados

# palavra = input("Digite uma palavra ")
# idade = int(input("Digite sua idade "))
# peso = float(input("Digite seu peso "))
# print(palavra)
# print(idade)
# print(peso)

# texto = input("Digite um texto: ")

# print(texto)
# print(texto.upper()) #Transforma em letra maiscula
# print(texto.lower()) #Transforma em letra minuscula
# print(texto.title()) #Transforma a primeira letra de todas as palavras
# print(texto.capitalize()) #Transforma a primeira letra do texto em maiscula
# print(texto.swapcase()) #Inverte
# print(texto)

# print(texto.find('w'))
# print(texto.rfind('a'))
# print(texto.index('a'))
# print(texto.rindex('a'))
# print(texto.count('a'))
# print(texto.replace('a','A',1))
# print(texto)

palavra = 'bonba'
id = palavra.rfind('b')
# print(id)
# print(palavra[id])
# print(palavra[id - 1])
# print(palavra[id - 1] == 'm')
# print(palavra.replace('n', 'm'))

texto = "Preto pobre é sempre esculachado."
# print(texto.replace('Preto', '****'))

# print("italosouzacampos99@gmail.com".startswith('i'))
# print(palavra.endswith('a'))

#Operadores Booleanos e Binários

z = 10
w = 10
#print(True and False)
print((z>=w) and (z>w))
#print(True and False)
print((z>=w) or (z>w))
#print(True and False) >> not >> #print(True and True)
print((z>=w) and not(z>w))

print(not((z>=w) and not(z>w)))

s = True
c = True
m = False

print(s and ((not(c) and m) or (c and not(m))))


#OPERADORES DE ATRIBUIÇÃO E IDENTIDADE
a = 10
a += 5 # a = a + 5
print(a)
a -= 2 # a = a - 2
print(a)
a *= 2 # a = a * 2
print(a)

nome = "python"
print('p' in nome)
print('P' not in nome)
linguagem = nome
print(linguagem)
print(linguagem is nome)
print(linguagem is not nome)
nome = "Java"
print(nome)
print(linguagem)

