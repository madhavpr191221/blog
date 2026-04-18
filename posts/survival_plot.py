import matplotlib.pyplot as plt
import numpy as np

# Dark theme
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Simulated Weibull survival curve
t = np.linspace(0, 12000, 1000)
S = np.exp(-(t/8000)**1.8)

ax.plot(t, S, color='#00BFFF', linewidth=2.5, label='Survival Function $S(t)$')

# Censored observations — tick marks on the curve
censored_times = [3200, 5500, 7100, 9800, 10000]
for ct in censored_times:
    s_val = np.exp(-(ct/8000)**1.8)
    ax.plot(ct, s_val, '|', color='#FF6B6B', markersize=14, markeredgewidth=2.5)

# Failed observations — dots on the curve
failed_times = [1205, 2341, 4678, 6102, 7823, 9441]
for ft in failed_times:
    s_val = np.exp(-(ft/8000)**1.8)
    ax.plot(ft, s_val, 'o', color='#FFD700', markersize=7)

ax.set_xlabel('Time (hours)', color='white', fontsize=13)
ax.set_ylabel('$S(t)$', color='white', fontsize=13)
ax.set_title('A Survival Guide to Survival Analysis', 
             color='white', fontsize=16, fontweight='bold', pad=20)
ax.legend(fontsize=11, loc='upper right')
ax.set_facecolor('#0d0d0d')
fig.patch.set_facecolor('#0d0d0d')

plt.tight_layout()
plt.savefig('cover.png', dpi=150, bbox_inches='tight')
plt.show()