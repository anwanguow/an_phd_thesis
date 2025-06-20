import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, MultiPolygon
import numpy as np

def plot_shapely_poly(ax, poly, color, alpha):
    if poly.is_empty:
        return
    if isinstance(poly, Polygon):
        patch = plt.Polygon(np.array(poly.exterior.coords), facecolor=color, alpha=alpha, edgecolor=None)
        ax.add_patch(patch)
        for interior in poly.interiors:
            hole = plt.Polygon(np.array(interior.coords), facecolor='white', edgecolor=None)
            ax.add_patch(hole)
    elif isinstance(poly, MultiPolygon):
        for p in poly.geoms:
            plot_shapely_poly(ax, p, color, alpha)

r1 = 1
r2 = 1 + 0.08
r3 = np.sqrt(4 / 3)
r4 = np.sqrt(4 / 3) + 0.15

r = r1

height = np.sqrt(3)
v0 = np.array([0, 0])
v1 = np.array([2, 0])
v2 = np.array([1, height])
centers = [v0, v1, v2]

circles = [Point(c).buffer(r, resolution=512) for c in centers]

pairwise_union = circles[0].intersection(circles[1]).union(circles[1].intersection(circles[2])).union(circles[2].intersection(circles[0]))
triple = circles[0].intersection(circles[1]).intersection(circles[2])
only_pairwise = pairwise_union.difference(triple)

fig, ax = plt.subplots(figsize=(6,6), dpi=300)

plot_shapely_poly(ax, only_pairwise, '#B0BEC5', 0.5)
plot_shapely_poly(ax, triple, '#FFB300', 0.7)

for c in centers:
    circle = plt.Circle(c, r, edgecolor='#B0BEC5', facecolor='none', linewidth=2)
    ax.add_patch(circle)

triangle = np.array([v0, v1, v2, v0])
plt.plot(triangle[:,0], triangle[:,1], 'k-', linewidth=2)

margin = 0.6
ax.set_aspect('equal')
plt.xlim(-r - margin, 2 + r + margin)
plt.ylim(-r - margin, height + r + margin)
plt.axis('off')
plt.tight_layout()
plt.show()
