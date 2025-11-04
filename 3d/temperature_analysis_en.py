import json
import matplotlib.pyplot as plt
import numpy as np

# Data: (temperature, valid_rate, novelty_rate, recovery_rate)
data = [
    (0.0, 0.889, 1.000, 0.889),  # 20251103_142702
    (0.1, 0.889, 1.000, 0.889),  # 20251103_124444
    (0.2, 0.926, 1.000, 0.926),  # 20251103_115017
    (0.3, 0.852, 1.000, 0.852),  # 20251103_121617
    (0.4, 0.963, 1.000, 0.963),  # 20251103_124444
    (0.5, 0.963, 1.000, 0.963),  # 20251103_135547
    (0.6, 1.000, 1.000, 1.000),  # 20251103_142131
    (0.7, 0.963, 1.000, 0.963),  # 20251102_214808
    (0.8, 0.926, 1.000, 0.926),  # 20251103_122531
    (0.9, 0.889, 1.000, 0.889),  # 20251103_125734
    (1.0, 0.963, 0.963, 0.926)   # 20251103_140028
]

# Sort by temperature
data.sort(key=lambda x: x[0])

# Extract data
temperatures = [d[0] for d in data]
valid_rates = [d[1] for d in data]
novelty_rates = [d[2] for d in data]
recovery_rates = [d[3] for d in data]

# Create chart
plt.figure(figsize=(12, 8))

# Plot three lines
plt.plot(temperatures, valid_rates, 'o-', label='Validity', linewidth=2, markersize=8)
plt.plot(temperatures, novelty_rates, 's-', label='Uniqueness', linewidth=2, markersize=8)
plt.plot(temperatures, recovery_rates, '^-', label='Recovery', linewidth=2, markersize=8)

# Add value labels
for i, temp in enumerate(temperatures):
    plt.annotate(f'{valid_rates[i]:.3f}', (temp, valid_rates[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{novelty_rates[i]:.3f}', (temp, novelty_rates[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{recovery_rates[i]:.3f}', (temp, recovery_rates[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Set chart properties
plt.xlabel('Temperature Parameter', fontsize=14)
plt.ylabel('Performance Metrics', fontsize=14)
plt.title('Impact of Temperature Parameter on 3D Voxel Reconstruction Task Performance', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(np.arange(0, 1.1, 0.1))

# Set y-axis range
plt.ylim(0.8, 1.05)

# Optimize layout
plt.tight_layout()

# Save chart
plt.savefig('temperature_analysis_en.png', dpi=300, bbox_inches='tight')
plt.savefig('temperature_analysis_en.svg', dpi=300, bbox_inches='tight')

print("Chart generated and saved as temperature_analysis_en.png and temperature_analysis_en.svg")