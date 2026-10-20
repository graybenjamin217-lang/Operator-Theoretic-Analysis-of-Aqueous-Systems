import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

fig, ax = plt.subplots(figsize=(8, 5))
delta_x = np.linspace(0, 0.6, 500)
noise_response = np.exp(-3 * delta_x) * (1 + 5 * np.maximum(0, delta_x - 0.27417)**2)

ax.plot(delta_x, noise_response, color='#d62728', linewidth=2, label='Shear Noise Energy')
ax.axvline(x=0.27417, color='#7f7f7f', linestyle='--', linewidth=1.5, label='Critical Threshold (delta_crit approx 0.27417)')
ax.fill_between(delta_x, 0, noise_response, where=(delta_x <= 0.27417), color='#ff9896', alpha=0.3, label='Quadratic Suppression Zone')

ax.set_title('Figure 3: Non-Linear Feedback Operator Shear Noise Suppression', fontsize=11, fontweight='bold')
ax.set_xlabel('Deformation Parameter (||X||)', fontsize=10)
ax.set_ylabel('Dissipation / Noise Amplitude', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

fig.tight_layout()
fig.savefig('fig3_feedback_suppression.png', dpi=300)
plt.show()
