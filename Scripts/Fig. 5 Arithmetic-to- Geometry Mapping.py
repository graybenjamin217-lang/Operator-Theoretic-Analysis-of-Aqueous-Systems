import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Fixed import

plt.rcParams['font.family'] = 'serif'

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

W = 2  # Winding parameter
R_torus, r_tube = 3.0, 1.0
X_torus = (R_torus + r_tube * np.cos(W * theta)) * np.cos(phi)
Y_torus = (R_torus + r_tube * np.cos(W * theta)) * np.sin(phi)
Z_torus = r_tube * np.sin(W * theta)

surf = ax.plot_surface(X_torus, Y_torus, Z_torus, cmap='viridis', edgecolor='none', alpha=0.85)
ax.set_title('Figure 5: Arithmetic-to-Geometry Mapping (W in Z Topological Manifold)', fontsize=11, fontweight='bold')
ax.set_axis_off()

fig.tight_layout()
fig.savefig('fig5_arithmetic_geometry_bridge.png', dpi=300)
plt.show()
