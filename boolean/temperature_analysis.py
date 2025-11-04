import matplotlib.pyplot as plt
import numpy as np

# Data: (temperature, valid_rate, novelty_rate, recovery_rate)
data = [
    (0.0, 0.96, 0.96, 0.96),  # 20251103_175823
    (0.1, 0.96, 0.95, 0.95),  # 20251103_125412
    (0.2, 0.9566666666666667, 0.9199999999999999, 0.8866666666666667),  # 20251103_140746
    (0.3, 0.9800000000000001, 0.9800000000000001, 0.9800000000000001),  # 20251103_175802
    (0.4, 1.0, 0.8800000000000001, 0.8800000000000001),  # 20251103_175832
    (0.5, 0.99, 0.9700000000000001, 0.9700000000000001),  # 20251103_175843
    (0.6, 1.0, 0.8899999999999999, 0.8899999999999999),  # 20251103_175858
    (0.7, 1.0, 0.9800000000000001, 0.9800000000000001),  # 20251103_115215
    (0.8, 1.0, 0.8899999999999999, 0.8899999999999999),  # 20251103_123631
    (0.9, 1.0, 0.93, 0.93),  # 20251103_175907
    (1.0, 1.0, 0.9466666666666667, 0.9466666666666667)   # 20251103_175916
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
plt.plot(temperatures, valid_rates, marker='o', linewidth=2, label='Validity')
plt.plot(temperatures, novelty_rates, marker='s', linewidth=2, label='Uniqueness')
plt.plot(temperatures, recovery_rates, marker='^', linewidth=2, label='Recovery')

# Add labels and title
plt.xlabel('Temperature')
plt.ylabel('Performance Metrics')
plt.title('Impact of Temperature Parameter on Boolean Task Performance')
plt.legend()
plt.grid(True, alpha=0.3)

# Save as PNG
plt.savefig('temperature_analysis.png', dpi=300, bbox_inches='tight')
plt.savefig('temperature_analysis.svg', dpi=300, bbox_inches='tight')
plt.close()