import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

n = 20
x = np.linspace(1/(n+1), n/(n+1), n)

def W1(x, y):
    return x * y

def W2(x, y):
    return (x + y <= 1).astype(float)

A1 = np.zeros((n, n))
for i in range(n):
    for j in range(i+1, n):
        if W1(x[i], x[j]) > 0:
            A1[i, j] = 1
            A1[j, i] = 1
G1 = nx.from_numpy_array(A1)

plt.figure(figsize=(6, 6))
pos1 = nx.circular_layout(G1)
nx.draw(G1, pos1, node_color='blue', node_size=120, edge_color='gray')
plt.title(r"Graph from $W_1(x, y) = x \cdot y$", fontsize=18)
plt.tight_layout()
plt.show()

A2 = np.zeros((n, n))
for i in range(n):
    for j in range(i+1, n):
        if W2(x[i], x[j]) > 0:
            A2[i, j] = 1
            A2[j, i] = 1
G2 = nx.from_numpy_array(A2)

pos2 = nx.circular_layout(G2)

# Rotated 180°
for k in pos2:
    pos2[k] = -pos2[k]

plt.figure(figsize=(6, 6))
nx.draw(G2, pos2, node_color='green', node_size=120, edge_color='black')
plt.title(r"Graph from $W_2(x, y) = \mathbb{1}_{x+y \leq 1}$", fontsize=18)
plt.tight_layout()
plt.show()
