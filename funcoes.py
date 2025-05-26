# linguagem = 'Python'
# print(linguagem[2::5])
# print(linguagem[::5])
# print(linguagem[2:5])

# FUNÇÕES

def calcSoma(a, b):
    res = a+b
    return res
soma = calcSoma(3, 2)
print(soma)

def calcSoma2(*numeros): #Assim é bem mais fácil, pois não preciso declarar variáveis a todo instante.
    return sum(numeros)
print(calcSoma2(1,2,3,4,5,6,7,8,9,10))

def resposta(nome="Nome não informado", matricula="Aluno não informou a matricula"):
  return f"Prezada {nome} ({matricula}) sua nota..."

print(resposta(matricula="20251101", nome="Italo"))
print(resposta("italo", 21400000))

def cadastroPaciente(nome="Desconhecido", CPF="000.000.000-00", tel="(00)00000-0000"):
  mensagem = f"Seja bem vindo(a) {nome}.\nConfirmando seu CPF: {CPF}.\nEm breve retornaremos para o contato: {tel}\n"
  return mensagem

print(cadastroPaciente("Sandro", 31482937387, "(85)98818-2453"))
print(cadastroPaciente("Sandro", 31482937387))
print(cadastroPaciente(CPF=31482937387, tel="(85)98818-2453"))
print(cadastroPaciente(CPF=31482937387, nome="Sandro", tel="(85)98818-2453"))



# CONTINUAÇÃO DE DICIONÁRIO
pessoa = {'nome': "Italo", 'idade': 42, 'peso': 69.23, 'vivo': False}
print(pessoa)

# BUSCAR UM DADO NO DICIONÁRIO
print(pessoa["nome"])
print(pessoa.get("nome"))

# ATUALIZAR UM DADO NO DICIONÁRIO
pessoa["nome"] = "Pedro"
print(pessoa)
pessoa.update({"nome": "Carlos", "peso":98})
print(pessoa)

# ADICIONAR NOVO ÍTEM
pessoa["sobrenome"] = "Mesquita"
print(pessoa)

# DELETA DO DICIONÁRIO
del pessoa["sobrenome"]
print(pessoa)

# DELETA DO DICIONÁRIO, PORÉM TEM UM BACKUP
idade = pessoa.pop("idade")
print(pessoa)
print(idade)

for chave in pessoa.items():
   print(chave)