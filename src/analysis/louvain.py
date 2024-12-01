import pandas as pd
import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data\\processed\\resultado_expandido_limpo.csv')
G = nx.Graph()

# Add edges to graph from data
for index, row in data.iterrows():
    G.add_edge(row['pesquisador_id'], row['coautores'])

# Apply the Louvain algorithm to detect communities
partition = community_louvain.best_partition(G)

# Count nodes in each community
from collections import Counter
community_counts = Counter(partition.values())

# Prepare visualization
pos = nx.spring_layout(G)  # Spring layout for visualization
node_colors = [partition[node] for node in G.nodes()]
plt.figure(figsize=(12, 8))

# Draw the graph
nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=plt.cm.tab20, node_size=50)
nx.draw_networkx_edges(G, pos, alpha=0.5)

# Add community labels
for community_id, size in community_counts.items():
    # Find a representative node for each community
    representative_node = [node for node, comm in partition.items() if comm == community_id][0]
    x, y = pos[representative_node]
    plt.text(x, y, f"C{community_id}", fontsize=12, fontweight="bold", color="red")

# Plot adjustments
plt.title("Detecção de Comunidades com Louvain (Número das Comunidades)")
plt.axis("off")
plt.show()
