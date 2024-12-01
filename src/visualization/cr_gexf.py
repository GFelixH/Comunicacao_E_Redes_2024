import pandas as pd
import networkx as nx

expanded_df = pd.read_csv('data\\processed\\resultado_expandido_limpo.csv')

# Criar o MultiGraph
G = nx.MultiGraph()

# Adicionar arestas entre cada pesquisador e seus coautores
for _, row in expanded_df.iterrows():
    researcher = row['pesquisador_id']
    coauthor = row['coautores']
    G.add_edge(researcher, coauthor)

# Exibir informações sobre o grafo criado

nx.write_gexf(G, "src\\visualization\\multigrafo_nomes(2).gexfil")