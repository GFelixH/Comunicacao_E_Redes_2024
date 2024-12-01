import pandas as pd
import networkx as nx

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

# Get top 5 nodes for each centrality measure
top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
top_closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 by Degree Centrality:", top_degree)
print("Top 5 by Closeness Centrality:", top_closeness)
print("Top 5 by Betweenness Centrality:", top_betweenness)