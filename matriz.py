# Dimensão
# A dimensão é o número de coordenadas necessárias para definir um ponto no espaço.

# ✅ 1D (Uma dimensão) → Linha reta. Exemplo: posição em uma régua.
# ✅ 2D (Duas dimensões) → Plano cartesiano (x, y). Exemplo: um jogo 2D.
# ✅ 3D (Três dimensões) → Espaço tridimensional (x, y, z). Exemplo: um cubo no mundo real.
# ✅ 4D ou mais → Conceito teórico usado em física e computação.

# texto = vetor
# texto com hiperlink (link externo) = volume

#Matriz e Dicionário com lista
x,y,z,vol = 5,7,2,-1
vol = x * y * z
coordenadas = [x,y,z,vol]

print(f"Lado X do paralelepípedo: {coordenadas[0]}")
print(f"Lado Y do paralelepípedo: {coordenadas[1]}")
print(f"Lado Z do paralelepípedo: {coordenadas[2]}")
print(f"O volume do paralelepipedo é: {coordenadas[3]}")

add = ["Passaré","Desembargador Otacílio Peixoto", 200]
add2 = ["Parangaba","Suécia",252]
add3 = ["Aldeota","Godofredo Maciel",[560,"Bloco B"]]

adds = [add,add2,add3]
print(adds)
print(adds[1]) #1 dimensão
print(adds[1][2]) #2 dimensões
print(adds[2][2][1]) #3 dimensões

clientes = ["Sandro","Pedro","Paulo"]
print(clientes)


cliente_1 = ["1","100.000.000-00",2008,[-150,3,1593],False]
cliente_2 = ["2","200.000.000-00",2009,[90,65,2036],True]
cliente_3 = ["3","300.000.000-00",2010,[102,85,525],False]
clientes = [cliente_1,cliente_2,cliente_3]

for cli in clientes:
    print(cli)