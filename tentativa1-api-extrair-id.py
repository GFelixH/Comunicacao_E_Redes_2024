import requests
import pandas as pd
from time import sleep

# Carregar o CSV com nomes de pesquisadores
pesquisadores_df = pd.read_csv('autores_com_artigos.csv')

# Lista para armazenar os resultados
ids_pesquisadores = []

# Função para buscar o ID do OpenAlex para um autor pelo nome
def buscar_id_por_nome(nome):
    url = f'https://api.openalex.org/authors?mailto=diemaschinefelix@gmail.com?filter=display_name.search:{nome}'
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

# Loop para buscar o ID de cada pesquisador no OpenAlex
for _, row in pesquisadores_df.iterrows():
    nome = row['Nome']  # Usar a coluna "Nome" do CSV
    artigos = row['Quantidade de Artigos']
    autor_id, nome_encontrado = buscar_id_por_nome(nome)
    
    #Para controle por console
    print(f'interando nome {nome} e qnt-arigos {artigos}')
    print()
    
    
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
ids_df.to_csv('autores_com_id.csv', index=False)

print("Arquivo 'autores_com_id.csv' gerado com sucesso.")
