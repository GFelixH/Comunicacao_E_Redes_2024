import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data\\processed\\resultado_expandido_limpo.csv')
G = nx.Graph()

# Add edges to graph from data
for index, row in data.iterrows():
    G.add_edge(row['pesquisador_id'], row['coautores'])

# Calculate centralities
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Calculate clustering coefficient for each node
clustering_coefficients = nx.clustering(G)

# Calculate assortativity (degree assortativity coefficient)
assortativity_coefficient = nx.degree_assortativity_coefficient(G)

# Get top 5 nodes for each centrality measure
top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
top_closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
top_clustering = sorted(clustering_coefficients.items(), key=lambda x: x[1], reverse=True)[:5]

# Print results
print("Top 5 by Degree Centrality:", top_degree)
print("Top 5 by Closeness Centrality:", top_closeness)
print("Top 5 by Betweenness Centrality:", top_betweenness)
print("Top 5 by Clustering Coefficient:", top_clustering)
print("Assortativity Coefficient (Degree Assortativity):", assortativity_coefficient)

# Coeficiente local de clusterização
local_clustering = nx.clustering(G)
print("Coeficientes locais de clusterização:", local_clustering)

# Coeficiente médio de clusterização
average_clustering = nx.average_clustering(G)
print("Coeficiente médio de clusterização:", average_clustering)

# Gerando posições para os nós com spring_layout
pos = nx.spring_layout(G)  # Posições para todos os nós, calculadas automaticamente

# Desenhando o grafo
plt.figure(figsize=(10, 8))  # Opcional: Tamanho da figura
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')  # Cor e tamanho dos nós
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')  # Cor e transparência das arestas
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")  # Tamanho da fonte das labels

plt.title("Network Graph")
plt.axis('off')  # Desligando o eixo
plt.show()
