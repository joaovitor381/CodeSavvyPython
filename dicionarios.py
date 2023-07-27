"""Listas: Coleção ordenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionarios: Coleção não ordenada, mutável e que não permite valores duplicados
"""

lista = ["item2", "item3", "item2"]
tupla = ("item1", "item2", "item1")
dicio = {"chave1": "ozzy", "chave2": 2005, "chave3": True}

print(dicio)

dicionario = {
    "nome": "Jimmy Page",
    "idade": 36,
    "nacionalidade": "britanico"
}

print(dicionario)

print(dicionario["nome"])

print(dicionario.get("idade"))

print(dicionario.keys())  # Retorna todas as chaves que o dicionario possui

print(len(dicionario))  # Retorna quantas chaves tem no dicionario

print(dicionario.values())  # Retorna os valores das chaves

# chave:valor

dados = {"nome": "cia", "kgb": 111, "valor_logico": True}
dados.update({"movimento": "hippie"})
print(dados)


dados.popitem()  # elimina o último item dos dados "movimento"
print(dados)

dados.pop("kgb")  # elimina o elemento "kgb"
print(dados)

for x, y in dados.items():
    print(x, y)
