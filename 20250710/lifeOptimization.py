# %%
import matplotlib.pyplot as plt
import mpltern

# Define corners: I, E, C
# Example hypothetical paths (percentages must sum to 100)
paths = {
    "Deep Technical Role": [70, 20, 10],
    "Corporate Sales": [10, 70, 20],
    "Lifestyle Job": [20, 30, 50],
    "Your Estimate": [40, 40, 20]
}

# Triple point estimate
triple_point = [40, 40, 20]

# Create ternary plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='ternary')

# Plot points
for label, coords in paths.items():
    ax.scatter(*coords, label=label, s=80)

# Highlight triple point
ax.scatter(*triple_point, color='red', s=120, label='Viable Zone Estimate')

# Draw exploration vectors
# Example: small moves to test boundaries
explore_vectors = [
    [50, 30, 20],  # push more technical
    [30, 50, 20],  # push more economic
    [40, 30, 30]   # push for lower energy cost
]

for vec in explore_vectors:
    ax.scatter(*vec, color='gray', s=50)
    ax.plot([triple_point[0], vec[0]],
            [triple_point[1], vec[1]],
            [triple_point[2], vec[2]],
            color='gray', linestyle='--')

# Labels and formatting
ax.set_tlabel('Intrinsic Interest / Alignment')
ax.set_llabel('Economic Yield / Sustainability')
ax.set_rlabel('Energy Cost / Skill-Building Feasibility')

ax.legend()
plt.show()

# %%

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Grid of technical depth (0–10) and domain breadth (0–10)
x = np.linspace(0, 10, 100)  # Technical Depth
y = np.linspace(0, 10, 100)  # Domain Breadth
X, Y = np.meshgrid(x, y)

# Example fitness function:
# Peaks at moderate depth and moderate breadth (intersections)
Z = np.exp(-((X - 5)**2 + (Y - 5)**2) / 8)  # Gaussian peak
# Add multiple peaks for hybrid niches
Z += 0.5 * np.exp(-((X - 8)**2 + (Y - 3)**2) / 2)
Z += 0.3 * np.exp(-((X - 2)**2 + (Y - 7)**2) / 1.5)

# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
ax.set_xlabel('Technical Depth')
ax.set_ylabel('Domain Breadth / Interdisciplinarity')
ax.set_zlabel('Viability Fitness')

plt.title('Career Fitness Landscape')
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Axes: X = Tech Depth, Y = Breadth
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

# Your fitness function: broad peak at (6,6), narrower peaks at (8,4) and (4,9)
Z = np.exp(-((X - 6)**2 + (Y - 6)**2) / 4)
Z += 0.5 * np.exp(-((X - 8)**2 + (Y - 4)**2) / 2)
Z += 0.4 * np.exp(-((X - 4)**2 + (Y - 9)**2) / 2)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Current position
current = [5, 7]
ax.scatter(current[0], current[1], np.exp(-((current[0] - 6)**2 + (current[1] - 6)**2) / 4),
           color='red', s=80, label='Current Position')

# Draw vectors
vectors = [
    [6, 6],  # Stabilize
    [8, 4],  # Deep technical
    [4, 9]   # High breadth founder/operator
]

for vec in vectors:
    ax.scatter(vec[0], vec[1], np.exp(-((vec[0] - 6)**2 + (vec[1] - 6)**2) / 4),
               color='gray', s=50)
    ax.plot([current[0], vec[0]],
            [current[1], vec[1]],
            [np.exp(-((current[0] - 6)**2 + (current[1] - 6)**2) / 4),
             np.exp(-((vec[0] - 6)**2 + (vec[1] - 6)**2) / 4)],
            color='gray', linestyle='--')

ax.set_xlabel('Technical Depth')
ax.set_ylabel('Domain Breadth / Bridges')
ax.set_zlabel('Viability Fitness')

plt.title('Career Fitness Landscape: Transitional Equilibrium & Vectors')
ax.legend()
plt.show()

# %%
