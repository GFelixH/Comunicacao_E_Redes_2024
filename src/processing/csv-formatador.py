import csv

# Nome do arquivo de entrada e saída
arquivo_txt = "data\\raw\\autores_X_Artigos.txt"
arquivo_csv = "data\\raw\\autores_com_artigos.csv"

# Lista para armazenar os dados processados
dados = []

# Abrir o arquivo txt e ler as linhas
try:
    with open(arquivo_txt, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo_txt} não foi encontrado.")
    exit(1)

# Processar as linhas, pulando as duas primeiras e agrupando nome e quantidade de artigos
for i in range(2, len(linhas), 2):  # Começa na linha 3 (índice 2) e pula de 2 em 2
    nome = linhas[i].strip()        # Remover espaços em branco no início e fim da linha
    if i + 1 < len(linhas):         # Verifica se existe uma linha seguinte para o número de artigos
        artigos = linhas[i + 1].strip()
        
        # Verificar se o valor de artigos é um número válido
        if artigos.isdigit():
            dados.append([nome, artigos])
        else:
            print(f"Valor inválido para a quantidade de artigos: {artigos} para {nome}")

# Escrever os dados no arquivo CSV
with open(arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Quantidade de Artigos'])  # Cabeçalhos
    writer.writerows(dados)

print(f"Arquivo '{arquivo_csv}' gerado com sucesso.")
