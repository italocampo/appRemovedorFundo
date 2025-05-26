# CONJUNTOS EM PYTHON

lista = ["sandro", 42]
tupla = ("sandro", 42)
dicionario = {"nome": "sandro", "idade": 42}
conjunto = {"sandro", 42} #set

print(lista)
print(tupla)
print(dicionario)
print(conjunto)

letras = set(['a', 'b', 'c', 'd', 'e'])
print(letras)

dicionario["sobrenome"] = "mesquita"
print(dicionario)

#UNIÃO
A = {5, 6, 7, 8}
B = {7, 8, 9, 10}
C = A.union(B)
print(C)
print(A | B)

#DIFERENÇA
D = A.difference(B)
print(D)
print(A - B)

E = B.difference(A)
print(E)
print(B - A)

F = A.symmetric_difference(B)
print(F)
print(A ^ B)