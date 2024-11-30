import pandas as pd
import requests

# Função para obter o nome do autor a partir do ID
def obter_nome_autor(autor_id):
    url = f"https://api.openalex.org/authors/{autor_id.split('/')[-1]}"  # Extrai o ID do autor da URL
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        return dados.get('display_name', 'Nome não encontrado')
    else:
        print(f"Erro ao obter dados para {autor_id}")
        return None

# Carregar o CSV com os dados de coautoria
input_csv = "data/processed/resultado_coautoria_final.csv"  # Substitua pelo caminho correto do arquivo
df = pd.read_csv(input_csv)

# Lista para armazenar os resultados (pesquisador_id, coautores)
resultados = []

# Loop para processar cada linha do CSV
a=0
for _, row in df.iterrows():
    a = a + 1
    pesquisador_id = row['pesquisador_id']  # ID do pesquisador
    artigo_id = row['artigo_id']  # ID do artigo
    coautores = row['coautores']  # Lista de coautores (provavelmente uma string)
    
    # Limpar a string de coautores e transformar em uma lista
    coautores = coautores.strip("[]").replace("'", "").split(", ")

    # Adicionar o pesquisador_id e cada coautor para cada artigo
    for coautor in coautores:
        # Obter o nome do coautor
        nome_coautor = obter_nome_autor(coautor)
        if nome_coautor:
            resultados.append({
                'pesquisador_id': obter_nome_autor(pesquisador_id),  # Nome do pesquisador
                'coautores': nome_coautor  # Nome do coautor
            })
    if a > 5:
        break

# Criar um DataFrame com os resultados
df_resultado = pd.DataFrame(resultados)

# Salvar os resultados em um novo arquivo CSV
output_csv = "data/raw/pesquisador_com_coautores.csv"  # Substitua pelo caminho desejado
df_resultado.to_csv(output_csv, index=False)

print(f"Arquivo '{output_csv}' gerado com sucesso.")
