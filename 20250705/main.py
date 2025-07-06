# %%
## Plant fields
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Artistic 3D surface parameters
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)

# Create a dynamic, organic surface using sine, cosine, and a Gaussian envelope
Z = (
    np.sin(X) * np.cos(Y) +
    0.5 * np.sin(2*X + Y) +
    0.3 * np.cos(X - 2*Y) +
    np.exp(-0.1 * (X**2 + Y**2)) * np.sin(3*X + 2*Y)
)

fig = plt.figure(figsize=(10, 7), facecolor='#f8f6ed')
ax = fig.add_subplot(111, projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.7, alpha=0.7)

# Overlay colored contours at different topological levels
contour_levels = np.linspace(Z.min(), Z.max(), 10)
ax.contourf(X, Y, Z, zdir='z', offset=Z.min()-2, levels=contour_levels, cmap='viridis', alpha=0.7)

# Artistic tweaks
ax.set_axis_off()
ax.grid(False)
plt.tight_layout()
plt.show()
# %%
## Random smoke dynamics