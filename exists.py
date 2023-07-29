import os

# Lista de arquivos a serem verificados
arquivos = ["fatorial.py", "boolean.py", "primo.py", "concatenacao.py", "geradordesenhas.py"]

# Verificar a existência de cada arquivo e imprimir o resultado
for arquivo in arquivos:
    if os.path.exists(arquivo):
        print(f"O arquivo '{arquivo}' existe.")
    else:
        print(f"O arquivo '{arquivo}' não existe.")
