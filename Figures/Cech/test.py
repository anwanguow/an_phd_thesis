#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

n_points = 10
radius = 1.0
ball_radius = 0.65

angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
points = np.c_[radius * np.cos(angles), radius * np.sin(angles)]

fig, ax = plt.subplots(figsize=(6,6), dpi=300)
ax.set_aspect('equal')

for x, y in points:
    circle = plt.Circle((x, y), ball_radius, color='orange', alpha=0.4)
    ax.add_patch(circle)
    ax.plot(x, y, 'ko')

ax.plot(
    np.append(points[:,0], points[0,0]),
    np.append(points[:,1], points[0,1]),
    'k:', lw=0.8, alpha=0.3
)

ax.axis('off')
plt.tight_layout()
plt.show()
