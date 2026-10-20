import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

fig, ax = plt.subplots(figsize=(8, 5))
r_radius = np.linspace(0.01, 150, 400)
kappa = 1.0 / 16.0
qed_field = np.exp(-((r_radius - 100)**2) / (2 * 15**2)) * (kappa * 16)

ax.plot(r_radius, qed_field, color='#9467bd', linewidth=2, label='Coherence Amplitude Envelope')
ax.axvline(x=100, color='#2ca02c', linestyle=':', linewidth=1.5, label='Optimal Domain Boundary (~100 nm)')
ax.axhline(y=kappa, color='#8c564b', linestyle='--', linewidth=1, label='Normalization Invariant kappa = 1/16')

ax.set_title('Figure 4: QED Coherence Domain Profile Governed by Invariant kappa', fontsize=11, fontweight='bold')
ax.set_xlabel('Radial Distance (nm)', fontsize=10)
ax.set_ylabel('Phase-Locking Coherence Density', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

fig.tight_layout()
fig.savefig('fig4_qed_coherence.png', dpi=300)
plt.show()
