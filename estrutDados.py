# lista = [ ]
# dicionário = { }
# tupla = ( )

lista = ["Sandro", 42, 1.79, True, 'm']

print(lista[4])
print(type(lista[4]))
print(type(lista))

print(len(lista))

ap1, ap2, ap3, ar, mp, mf = 6, 8, 10, 0, 0, 0
#ap1 = ap2 = ap3 = ar = mp = mf = 0
notas = [ap1, ap2, ap3, ar, mp, mf]
#print(len(notas)-3)
mp = (ap1 + ap2 + ap3) / (len(notas)-3)
print(mp)

#notas = [ap1, ap2, ap3, mp, ar, mf]
notas = [0, 0, 0, 0, 0, 0]
notas[0] = float(input("Digite a nota da AP1: "))
notas[1] = float(input("Digite a nota da AP2: "))
notas[2] = float(input("Digite a nota da AP3: "))
notas[3] = (notas[0] + notas[1] + notas[2]) / 3
print(notas[3])
print(notas)

notas = {"AP1": 0, "AP2": 0, "AP3": 0, "MP": 0, "AR": 0, "MF": 0}
notas["AP3"] = float(input("Digite a nota da AP1: "))
print(notas)

#APPEND
valores = []
valores.append(5)
valores.append(8)
valores.append(10)

print(valores)
print(sum(valores))
print(len(valores))

media = sum(valores)/len(valores)
print(media)

#SORT E REVERSE
numeros = [6, 8, 2, 0, 6, 7, 5, 4, 10]
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

nomes = ["Sandro", "Paulo", "Andre", "pedin", "Pedro", "Pedrão", "Pedra"]
print(ord("ã"))
nomes.sort()
print(nomes)

#INSERT
nomes[3] = "Jose"
nomes.insert(2, "Carlos")
print(nomes)

#EXTEND
nomes.extend(["Marcos", "Marcos", "Marcos"])
print(nomes)

#REMOVE
nomes.remove("Marcos")
print(nomes)

#POP
nomes.pop(2)
print(nomes)

#CLEAR
nomes.clear()
print(nomes)

#INDEX
cidades = ["FOR", "SP", "RJ", "SP", "FOR", "FOR", "NATAL", "CAUCAIA", "EUSEBIO"]
cidades.index("SP")

#COUNT
cidades.count("FOR")

horario = []
for hora in range(8, 18):
  #print(hora)
  horario.append(hora)
  #print(horario)
print(horario)

#LIST COMPRESSION
horario = [hora**2 for hora in range(8, 18)]
print(horario)

print(horario[:5])
print(horario[2:])
print(horario[2:5])

def soma(a, b):
  return a + b

print(soma(5, 10))

soma_lambda = lambda a, b: a + b
print(soma_lambda(5, 10))

lista = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(lista)

#FILTER

numeros = []
while True:
  numeros.append(float(input("Digite um numero: ")))
  print(numeros)
  media = sum(numeros)/len(numeros)
  print(media)