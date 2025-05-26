lista = ['FOR', 'SP', 'NATAL', 'FOR', 'FOR', 'RECIFE', 'NATAL', 'JP']
print(lista.count('SP'))
print(lista.index('SP'))
print(lista)

palavra = "bonba"
id = palavra.rfind('b')
print(id)
print(palavra[id])
print(palavra[id-1])
print(palavra[id-1] == 'm')
print(palavra.replace('n', 'm'))

texto = "O cara é preto ai por conta disso caiu no chao preto de calça e sapato preto"
print(texto.replace("preto", "****"))

print(" contato@profsandromesquita.com".startswith(' '))
print(palavra.endswith('a'))

num = input("Digite um numero: ")
print(num.isnumeric())