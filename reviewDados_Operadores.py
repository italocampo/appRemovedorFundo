letra = '1'
letra_decimal = ord(letra) #Converte para decimal
print(letra_decimal)
letra_minuscula = letra_decimal + 32 #+32 transforma em minúscula e -32 em maiúscula
print(letra_minuscula)
letra_minuscula_char = chr(letra_minuscula) #Converte para caractere
print(letra_minuscula_char)

#Transforme a primeira letra da palavra em maiúscula

palavra = 'sandro'
print (chr(ord(palavra[0])-32))

#Explicação:

#palavra[0] pega o primeiro caractere da string, que é 's'.
#ord('s') converte 's' para seu valor decimal na tabela ASCII, que é 115.
#ord('s') - 32 resulta em 83, que é o valor ASCII de 'S'.
#chr(83) converte esse número de volta para um caractere, que é 'S'.
#print('S') exibe S na tela.