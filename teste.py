import networkx as nx
import matplotlib.pyplot as plt

# Cria o grafo
G = nx.DiGraph()  # DiGraph para um grafo direcionado, onde a relação tem sentido (ex: manipulação)

# Lista de conexões de personagens no formato (Fonte, Destino, Relação)
connections = [
    ("Edward Richtofen", "Tank Dempsey", "Ally"),
    ("Edward Richtofen", "Nikolai Belinski", "Ally"),
    ("Edward Richtofen", "Takeo Masaki", "Ally"),
    ("Edward Richtofen", "Dr. Maxis", "Rival"),
    ("Edward Richtofen", "Samantha Maxis", "Manipulation"),
    ("Edward Richtofen", "Monty", "Manipulation"),
    ("Edward Richtofen", "Shadowman", "Manipulation"),
    ("Tank Dempsey", "Nikolai Belinski", "Ally"),
    ("Tank Dempsey", "Takeo Masaki", "Ally"),
    ("Dr. Maxis", "Samantha Maxis", "Family"),
    ("Dr. Maxis", "Monty", "Influence"),
    ("Samantha Maxis", "Edward Richtofen", "Rival"),
    ("Samantha Maxis", "Shadowman", "Manipulation"),
    ("Nikolai Belinski", "Takeo Masaki", "Ally"),
    ("Nikolai Belinski", "Tank Dempsey", "Ally"),
    ("Monty", "Shadowman", "Rival"),
    ("Monty", "Edward Richtofen", "Manipulation"),
    ("Shadowman", "Edward Richtofen", "Influence"),
    ("Shadowman", "Samantha Maxis", "Influence"),
    ("Shadowman", "The Warden", "Ally"),
    ("The Warden", "Shadowman", "Ally"),
    ("The Warden", "Tank Dempsey", "Enemy"),
    ("Takeo Masaki", "Monty", "Influence"),
    ("Takeo Masaki", "Shadowman", "Enemy"),
    ("Tank Dempsey", "The Warden", "Enemy"),
    ("Sophia", "Dr. Maxis", "Ally"),
    ("Sophia", "Edward Richtofen", "Conflict"),
    ("Pernell", "Samantha Maxis", "Manipulation"),
    ("Pernell", "Shadowman", "Influence"),
    ("Pernell", "Monty", "Enemy"),
    ("Pernell", "The Warden", "Ally"),
    ("Victis Group", "Edward Richtofen", "Ally"),
    ("Victis Group", "Samantha Maxis", "Conflict"),
    ("Victis Group", "Monty", "Influence"),
    ("Victis Group", "The Warden", "Enemy"),
    ("Ultimis Group", "Victis Group", "Ally"),
    ("Ultimis Group", "Edward Richtofen", "Ally"),
    ("Primis Group", "Ultimis Group", "Ally"),
    ("Primis Group", "Shadowman", "Enemy"),
    ("Shadowman", "Marlton Johnson", "Influence"),
    ("Marlton Johnson", "Russman", "Ally"),
    ("Russman", "Stuhlinger", "Ally"),
    ("Stuhlinger", "Edward Richtofen", "Manipulation"),
]

# Adiciona as arestas e os tipos de relacionamento como atributos
for source, target, relationship in connections:
    G.add_edge(source, target, relationship=relationship)

# Define cores para os tipos de relações
colors = {
    "Ally": "green",
    "Rival": "red",
    "Manipulation": "purple",
    "Influence": "orange",
    "Family": "blue",
    "Conflict": "gray",
    "Enemy": "black",
}

# Define a cor de cada aresta
edge_colors = [colors[G[u][v]['relationship']] for u, v in G.edges]

# Desenha o grafo
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)  # Layout do grafo

# Desenha os nós e arestas
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1000, edgecolors="black")
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrowstyle="->", arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

# Adiciona legenda para as cores
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color=color, lw=2, label=relationship) for relationship, color in colors.items()]
plt.legend(handles=legend_elements, loc="upper left")

plt.title("Grafo de Relações entre Personagens do Modo Zombies de Call of Duty")
plt.axis("off")  # Remove os eixos
plt.show()
import networkx as nx

# Cria o grafo e adiciona as conexões
G = nx.DiGraph()

connections = [
    ("Edward Richtofen", "Tank Dempsey", "Ally"),
    ("Edward Richtofen", "Nikolai Belinski", "Ally"),
    ("Edward Richtofen", "Takeo Masaki", "Ally"),
    ("Edward Richtofen", "Dr. Maxis", "Rival"),
    ("Edward Richtofen", "Samantha Maxis", "Manipulation"),
    ("Edward Richtofen", "Monty", "Manipulation"),
    ("Edward Richtofen", "Shadowman", "Manipulation"),
    ("Tank Dempsey", "Nikolai Belinski", "Ally"),
    ("Tank Dempsey", "Takeo Masaki", "Ally"),
    ("Dr. Maxis", "Samantha Maxis", "Family"),
    ("Dr. Maxis", "Monty", "Influence"),
    ("Samantha Maxis", "Edward Richtofen", "Rival"),
    ("Samantha Maxis", "Shadowman", "Manipulation"),
    ("Nikolai Belinski", "Takeo Masaki", "Ally"),
    ("Nikolai Belinski", "Tank Dempsey", "Ally"),
    ("Monty", "Shadowman", "Rival"),
    ("Monty", "Edward Richtofen", "Manipulation"),
    ("Shadowman", "Edward Richtofen", "Influence"),
    ("Shadowman", "Samantha Maxis", "Influence"),
    ("Shadowman", "The Warden", "Ally"),
    ("The Warden", "Shadowman", "Ally"),
    ("The Warden", "Tank Dempsey", "Enemy"),
    ("Takeo Masaki", "Monty", "Influence"),
    ("Takeo Masaki", "Shadowman", "Enemy"),
    ("Tank Dempsey", "The Warden", "Enemy"),
    ("Sophia", "Dr. Maxis", "Ally"),
    ("Sophia", "Edward Richtofen", "Conflict"),
    ("Pernell", "Samantha Maxis", "Manipulation"),
    ("Pernell", "Shadowman", "Influence"),
    ("Pernell", "Monty", "Enemy"),
    ("Pernell", "The Warden", "Ally"),
    ("Victis Group", "Edward Richtofen", "Ally"),
    ("Victis Group", "Samantha Maxis", "Conflict"),
    ("Victis Group", "Monty", "Influence"),
    ("Victis Group", "The Warden", "Enemy"),
    ("Ultimis Group", "Victis Group", "Ally"),
    ("Ultimis Group", "Edward Richtofen", "Ally"),
    ("Primis Group", "Ultimis Group", "Ally"),
    ("Primis Group", "Shadowman", "Enemy"),
    ("Shadowman", "Marlton Johnson", "Influence"),
    ("Marlton Johnson", "Russman", "Ally"),
    ("Russman", "Stuhlinger", "Ally"),
    ("Stuhlinger", "Edward Richtofen", "Manipulation"),
]

# Adiciona arestas ao grafo
for source, target, relationship in connections:
    G.add_edge(source, target)

# 1. Calcula a betweenness centrality para Edward Richtofen
betweenness = nx.betweenness_centrality(G)
print("Betweenness Centrality de Edward Richtofen:", betweenness["Edward Richtofen"])

# 2. Calcula a distância média dos menores caminhos
average_shortest_path_length = nx.average_shortest_path_length(G.to_undirected())
print("Média dos menores caminhos:", average_shortest_path_length)

# 3. Verifica se o grafo é de mundo pequeno
# Coeficiente de clustering
clustering_coefficient = nx.average_clustering(G.to_undirected())
print("Coeficiente de clustering médio:", clustering_coefficient)

# Diâmetro do grafo (maior menor caminho)
diameter = nx.diameter(G.to_undirected())
print("Diâmetro do grafo:", diameter)
