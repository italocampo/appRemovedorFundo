aluno = {
    "nome": ["Sandro", "Pedro", "Carlos"],
    "ano_nasc": [1982, 2000, 2020],
    "cpf": ["31482937387", "31482937300", "21482937387"],
    "sexo": ['m', 'm', 'm'],
    "status": [True, False, False]
}

print(aluno["nome"][1])
print(aluno.keys())
print(aluno.items())
aluno["email"] = ["none", "none", "danda@soprosex.com"]
print(aluno)

turma = {
    "20251100": {"nome": "Sandro", "ano_nasc": 1982, "cpf": "31482937387", "sexo": 'm', "status": True},
    "20251101": {"nome": "Pedro", "ano_nasc": 2000, "cpf": "31482937300", "sexo": 'm', "status": False},
    "20251102": {"nome": "Marcos", "ano_nasc": 1900, "cpf": "31482930000", "sexo": 'f', "status": True}
}

print(turma["20251100"]["nome"])
print(turma.keys())
print(turma.items())
turma["20251103"] = {"nome": "Marcos", "ano_nasc": 1900, "cpf": "31482930000", "sexo": 'f', "status": True}
turma["20251100"]["email"] = "sandro@profsandromesquita.com"
turma["20251101"]["email"] = "sandroca@profsandromesquita.com"
turma["20251102"]["email"] = "sandrinho@profsandromesquita.com"
turma["20251103"]["email"] = "sandreco@profsandromesquita.com"
print(turma)