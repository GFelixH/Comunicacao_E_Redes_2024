import csv

# Nome do arquivo de entrada e saída
arquivo_txt = 'autoresxartigos.txt'
arquivo_csv = 'autores_com_artigos.csv'

# Lista para armazenar os dados processados
dados = []

# Abrir o arquivo txt e ler as linhas
with open(arquivo_txt, 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Processar as linhas, pulando as duas primeiras e agrupando nome e quantidade de artigos
for i in range(2, len(linhas), 2):  # Começa na linha 3 (índice 2) e pula de 2 em 2
    nome = linhas[i].strip()  # Remover espaços em branco no início e fim da linha
    if i + 1 < len(linhas):  # Verifica se existe uma linha seguinte para o número de artigos
        artigos = linhas[i + 1].strip()
        dados.append([nome, artigos])

# Escrever os dados no arquivo CSV
with open(arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Quantidade de Artigos'])  # Cabeçalhos
    writer.writerows(dados)

print(f"Arquivo '{arquivo_csv}' gerado com sucesso.")





""" import csv

# Nome dos arquivos
arquivo_txt = 'autoresxartigos.txt'
arquivo_csv = 'resultado.csv'

# Lista para armazenar os dados processados
dados = []

# Abrir o arquivo txt e ler as linhas
with open(arquivo_txt, encoding="utf16-le") as file:
    linhas = file.readlines()

# Processar as linhas, pulando as duas primeiras e agrupando nome e quantidade de artigos
for i in range(2, len(linhas), 2):  # Começa na linha 3 (índice 2) e pula de 2 em 2
    nome = linhas[i].strip()  # Remover espaços em branco no início e fim da linha
    if i + 1 < len(linhas):  # Verifica se existe uma linha seguinte para o número de artigos
        artigos = linhas[i + 1].strip()
        dados.append([nome, artigos])

# Escrever os dados no arquivo CSV
with open(arquivo_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Quantidade de Artigos'])  # Cabeçalhos
    writer.writerows(dados)

print(f"Arquivo '{arquivo_csv}' gerado com sucesso.") """