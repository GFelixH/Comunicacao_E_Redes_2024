import requests
import pandas as pd
from time import sleep

# Carregar o CSV com nomes de pesquisadores
pesquisadores_df = pd.read_csv('autores_com_artigos.csv')

# Lista para armazenar os resultados
ids_pesquisadores = []

# Função para buscar ID de um pesquisador pelo nome
def buscar_id_por_nome(nome):
    url = f'https://api.openalex.org/authors?filter=display_name.search:{nome}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        # Verificar se há resultados e pegar o ID do primeiro
        if dados['meta']['count'] > 0:
            autor = dados['results'][0]  # Primeiro resultado
            return autor['id'], autor['display_name']
        else:
            print(f"Não encontrado: {nome}")
            return None, nome
    else:
        print(f"Erro na requisição para {nome}")
        return None, nome

# Loop através de cada pesquisador para buscar o ID
for _, row in pesquisadores_df.iterrows():
    nome = row['Nome']
    autor_id, nome_encontrado = buscar_id_por_nome(nome)
    ids_pesquisadores.append({
        'nome_original': nome,
        'nome_encontrado': nome_encontrado,
        'openalex_id': autor_id
    })
    # Espera para evitar sobrecarregar a API
    sleep(1)

# Salvar os resultados em um DataFrame ou CSV
ids_df = pd.DataFrame(ids_pesquisadores)
ids_df.to_csv('pesquisadores_com_id.csv', index=False)
