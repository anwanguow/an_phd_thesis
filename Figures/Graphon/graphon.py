import numpy as np
import matplotlib.pyplot as plt

n = 300
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)

W1 = X * Y
W2 = (X + Y <= 1).astype(float)

plt.figure(figsize=(5, 4))
im1 = plt.imshow(
    W1, origin='lower', extent=[0, 1, 0, 1],
    cmap='viridis', vmin=0, vmax=1
)
plt.title(r'$W_1(x,y)=x\cdot y$')
plt.colorbar(im1, label=r'$W_1(x,y)$')
plt.axis('off')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 4))
im2 = plt.imshow(
    W2, origin='lower', extent=[0, 1, 0, 1],
    cmap='viridis', vmin=0, vmax=1
)
plt.title(r'$W_2(x,y)=\mathbf{1}_{\{x+y\leq1\}}$')
plt.colorbar(im2, label=r'$W_2(x,y)$')
plt.axis('off')
plt.tight_layout()
plt.show()
