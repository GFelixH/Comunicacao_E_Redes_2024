import requests
import pandas as pd
from time import sleep


# Carregar o CSV com nomes de pesquisadores
pesquisadores_df = pd.read_csv("data\\raw\\autores_com_artigos.csv")

# Lista para armazenar os resultados
ids_pesquisadores = []

# Função para buscar o ID do OpenAlex para um autor pelo nome
def buscar_id_por_nome(nome):
    url = f'https://api.openalex.org/authors?filter=display_name.search:"{nome}"'  # Corrigir a URL
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        # Verificar se há resultados e pegar o ID do primeiro
        if dados['meta']['count'] > 0:
            # Verificar todos os autores encontrados e escolher um baseado em algum critério
            for autor in dados['results']:
                # Imprimir todos os resultados encontrados para análise
                print(f'Encontrado: {autor["display_name"]} com ID {autor["id"]}')
            # Retornar o primeiro resultado por enquanto
            return dados['results'][0]['id'], dados['results'][0]['display_name']
        else:
            print(f"Não encontrado: {nome}")
            return None, nome
    else:
        print(f"Erro na requisição para {nome}: {response.status_code}")
        return None, nome

# Loop para buscar o ID de cada pesquisador no OpenAlex
for _, row in pesquisadores_df.iterrows():
    nome = row['Nome']  # Usar a coluna "Nome" do CSV
    artigos = row['Quantidade de Artigos']
    autor_id, nome_encontrado = buscar_id_por_nome(nome)
    
    # Para controle por console
    print(f'Iterando nome: {nome} e quantidade de artigos: {artigos}')
    
    ids_pesquisadores.append({
        'Nome Original': nome,
        'Nome Encontrado': nome_encontrado,
        'OpenAlex_ID': autor_id,
        'Quantidade de Artigos': artigos
    })
    # Espera para evitar sobrecarregar a API
    sleep(1)  # Aguardar 1 segundo entre requisições

# Salvar os resultados em um novo CSV
ids_df = pd.DataFrame(ids_pesquisadores)
ids_df.to_csv('data/processed/autores_com_id2.csv', index=False)

print("Arquivo 'autores_com_id2.csv' gerado com sucesso.")
