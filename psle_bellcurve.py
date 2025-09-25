import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


plt.figure(figsize=(12, 8))


x = np.linspace(4, 32, 1000)


mean1, std1 = 16, 4
curve1 = norm.pdf(x, mean1, std1)


mean2, std2 = 11, 4
curve2 = norm.pdf(x, mean2, std2)


scale_factor = 40
curve1 *= scale_factor
curve2 *= scale_factor


plt.plot(x, curve1, 'b-', linewidth=3, label='Prelim SCORE', alpha=0.7)
plt.plot(x, curve2, 'r-', linewidth=3, label='PSLE SCORE', alpha=0.7)


plt.axvline(x=16, color='blue', linestyle='--', alpha=0.5, label='Median (16)')
plt.axvline(x=11, color='red', linestyle='--', alpha=0.5, label='Median (11)')
#Created by Gao Le

plt.xlabel('AL SCORE', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.title('PSLE VS PRELIM MEDIAN SCORE (SCHOOLS)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)


plt.xlim(4, 32)
plt.xticks(np.arange(4, 33, 2))


plt.tight_layout()
plt.show()
