import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

fig, ax = plt.subplots(figsize=(8, 5))
k_steps = np.arange(1, 7)
primorial_values = np.cumprod([2, 3, 5, 7, 11, 13])[:6]
scaling_curve = np.log(primorial_values)

ax.plot(k_steps, scaling_curve, marker='o', color='#1f77b4', linewidth=2, label='Primorial Milestones ln(P_k#)')
ax.bar(k_steps, scaling_curve * 0.3, alpha=0.3, color='#aec7e8', label='Discrete Operator Fiber Space')
ax.set_title('Figure 1: Primorial Spectral Dilation Generator (D_k) Step-Wise Expansion', fontsize=11, fontweight='bold')
ax.set_xlabel('Index Step (k)', fontsize=10)
ax.set_ylabel('Metric Scaling Magnitude', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left')

fig.tight_layout()
fig.savefig('fig1_primorial_dilation.png', dpi=300)
plt.show()
