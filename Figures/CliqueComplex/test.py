import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Polygon
import numpy as np

outer_N = 8
inner_N = 8
r_outer = 2.4
r_inner = 1.1

outer_pts = [(r_outer*np.cos(2*np.pi*i/outer_N), r_outer*np.sin(2*np.pi*i/outer_N)) for i in range(outer_N)]
inner_pts = [(r_inner*np.cos(2*np.pi*i/inner_N)+0.3*np.cos(2*np.pi*i/outer_N), r_inner*np.sin(2*np.pi*i/inner_N)+0.2*np.sin(2*np.pi*i/outer_N)) for i in range(inner_N)]

node_pos = {}
for i, xy in enumerate(outer_pts):
    node_pos[i] = xy
for i, xy in enumerate(inner_pts):
    node_pos[outer_N+i] = xy

G = nx.Graph()
for i in range(outer_N):
    G.add_edge(i, (i+1)%outer_N)
for i in range(inner_N):
    G.add_edge(outer_N+i, outer_N+(i+1)%inner_N)
for i in range(outer_N):
    G.add_edge(i, outer_N+i)
    G.add_edge(i, outer_N+((i-1)%outer_N))

missing_edges = [(1, 8), (3, 10), (6, 13)]
for e in missing_edges:
    if G.has_edge(*e):
        G.remove_edge(*e)

k4_offset = (3.6, 1.4)
K4_nodes = [outer_N+inner_N+j for j in range(4)]
K4_pos = {
    K4_nodes[0]: (k4_offset[0]+0, k4_offset[1]+0.5),
    K4_nodes[1]: (k4_offset[0]+1, k4_offset[1]+1.2),
    K4_nodes[2]: (k4_offset[0]+0.2, k4_offset[1]+2),
    K4_nodes[3]: (k4_offset[0]+1.1, k4_offset[1]+1.8)
}
for i in K4_nodes:
    node_pos[i] = K4_pos[i]
K4_edges = [(i, j) for i in K4_nodes for j in K4_nodes if i < j]
G.add_edges_from(K4_edges)
G.add_edge(0, K4_nodes[0])
pos = node_pos.copy()

cliques3 = [cl for cl in nx.find_cliques(G) if len(cl) == 3]
cliques4 = [cl for cl in nx.find_cliques(G) if len(cl) == 4]
cliques4 = [cl for cl in cliques4 if set(cl) == set(K4_nodes)]

plt.figure(figsize=(9, 7), dpi=300)
nx.draw_networkx_edges(G, pos, alpha=0.4, width=1.2)
nx.draw_networkx_nodes(G, pos, node_color='firebrick', node_size=52)

fill_colors = ['#7cc2f5', '#bae1ff', '#b3aee9', '#a4e8ba', '#f7e9a0', '#ffc09f', '#fcf5b6']

color_count = len(fill_colors)
for idx, clique in enumerate(cliques3):
    if set(clique) == set(K4_nodes):
        continue
    pts = [pos[v] for v in clique]
    polygon = Polygon(pts, closed=True, alpha=0.7, color=fill_colors[idx % color_count], edgecolor='gray', linewidth=1)
    plt.gca().add_patch(polygon)

if cliques4:
    for face in [(K4_nodes[0], K4_nodes[1], K4_nodes[2]),
                 (K4_nodes[0], K4_nodes[1], K4_nodes[3]),
                 (K4_nodes[0], K4_nodes[2], K4_nodes[3]),
                 (K4_nodes[1], K4_nodes[2], K4_nodes[3])]:
        pts = [pos[v] for v in face]
        polygon = Polygon(pts, closed=True, alpha=0.8, color='#ffe067', edgecolor='#a08400', lw=2)
        plt.gca().add_patch(polygon)
nx.draw_networkx_edges(G, pos, edgelist=K4_edges, width=2.6, edge_color='#a08400', alpha=0.9)

plt.axis('off')
plt.tight_layout()
plt.show()
