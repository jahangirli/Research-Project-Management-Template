"""
Generate all Figures!
"""

# Saving Figure
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(range(5), range(5), s=50, c='b')
plt.savefig("../outputs/figures/chart.pdf")

