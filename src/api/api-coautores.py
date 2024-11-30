import requests
import pandas as pd
from time import sleep

# Carregar o CSV
pesquisadores_df = pd.read_csv("data\\processed\\autores_com_id2.csv")

# Inicializar a lista para armazenar os resultados de coautoria
resultados_coautoria = []

# Função para obter artigos de um pesquisador específico
def obter_coautoria(pesquisador_id):
    url = f'https://api.openalex.org/works?filter=author.id:{pesquisador_id},from_publication_date:2018-01-01'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return dados.get('results', [])
    else:
        print(f"Erro na requisição para o pesquisador {pesquisador_id}")
        return []

# Loop através de cada pesquisador para obter dados de coautoria
for _, row in pesquisadores_df.iterrows():
    pesquisador_id = row['OpenAlex_ID']  # Coluna com o ID OpenAlex
    artigos = obter_coautoria(pesquisador_id)
    
    # Para controle por console
    print(f'Iterando sobre pesquisador ID {pesquisador_id}')
    print()

    for artigo in artigos:
        coautores = [autor['author']['id'] for autor in artigo['authorships'] if autor['author']['id'] != pesquisador_id]
        resultados_coautoria.append({
            'pesquisador_id': pesquisador_id,
            'artigo_id': artigo['id'],
            'coautores': coautores
        })
    
    # Espera para não sobrecarregar a API
    sleep(1)

# Salvar os resultados em um novo DataFrame ou CSV
resultados_df = pd.DataFrame(resultados_coautoria)
resultados_df.to_csv('data\\processed\\resultado_coautoria_final.csv', index=False)

