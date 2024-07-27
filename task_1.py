import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (аеропортів)
airports = ["JFK", "LAX", "ORD", "DFW", "DEN", "ATL", "SFO", "SEA", "MIA", "PHX"]
G.add_nodes_from(airports)

# Додавання ребер (сполучень між аеропортами)
connections = [
    ("JFK", "LAX"), ("JFK", "ORD"), ("JFK", "ATL"),
    ("LAX", "SFO"), ("LAX", "SEA"),
    ("ORD", "DFW"), ("ORD", "DEN"),
    ("DFW", "PHX"), ("DFW", "ATL"),
    ("DEN", "PHX"), ("DEN", "SEA"),
    ("ATL", "MIA"), ("ATL", "PHX"),
    ("SFO", "SEA")
]
G.add_edges_from(connections)

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_color="black", font_weight="bold")
plt.title("Airport Network Graph")
plt.show()

# Аналіз основних характеристик графа
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Degrees: {dict(G.degree())}")
print(f"Average degree: {sum(dict(G.degree()).values()) / G.number_of_nodes()}")
print(f"Clustering coefficient: {nx.average_clustering(G)}")
print(f"Density: {nx.density(G)}")
