
# %%
import numpy as np
import matplotlib.pyplot as plt

# Simulate two sensor estimates and variances
x1, x2 = 2.0, 5.0
var1, var2 = 1.0, 0.5

# Free energy landscape: sum of squared prediction errors weighted by inverse variance
x = np.linspace(0, 7, 400)
free_energy = ((x - x1)**2) / var1 + ((x - x2)**2) / var2

# Fused estimate (minimum free energy)
x3 = (x1/var1 + x2/var2) / (1/var1 + 1/var2)

plt.figure(figsize=(8, 4))
plt.plot(x, free_energy, label='Free Energy Landscape')
plt.axvline(x1, color='blue', linestyle='--', label='Sensor 1')
plt.axvline(x2, color='green', linestyle='--', label='Sensor 2')
plt.axvline(x3, color='red', linestyle='-', label='Fused Estimate (Min Free Energy)')
plt.scatter([x3], [((x3 - x1)**2)/var1 + ((x3 - x2)**2)/var2], color='red', zorder=5)
plt.xlabel('State Estimate')
plt.ylabel('Free Energy')
plt.title('Friston Free Energy Principle as Sensor Fusion')
plt.legend()
plt.show()


# %%
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
ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.7, alpha=0.7)

# Artistic tweaks
ax.set_axis_off()
ax.grid(False)
plt.tight_layout()
plt.show()
# %%
