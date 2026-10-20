import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

fig, ax = plt.subplots(figsize=(8, 5))
sectors = ['Core Sector\n(K = +2)', 'Neutral Sector\n(K = 0)', 'Peripheral Sector\n(K = -2)']
degeneracy_weights = [4, 8, 4]
colors = ['#ff7f0e', '#2ca02c', '#1f77b4']

bars = ax.bar(sectors, degeneracy_weights, color=colors, width=0.5, edgecolor='#333333', linewidth=1)
ax.set_title('Figure 2: 4:8:4 Eigenspace Degeneracy Split in Composite Manifold', fontsize=11, fontweight='bold')
ax.set_ylabel('Eigenspace Dimension Weight', fontsize=10)
ax.set_ylim(0, 10)
ax.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}-fold',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontweight='bold')

fig.tight_layout()
fig.savefig('fig2_eigenspace_degeneracy.png', dpi=300)
plt.show()
