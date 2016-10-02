import numpy as np
import matplotlib.pyplot as plt

x_vals = np.array([x for x in range(5, 31)])
y_vals = np.array([0.005, 0.004, 0.003, 0.004, 0.004, 0.005, 0.005, 0.005, 0.005, 0.005, 0.006, 0.005, 0.005, 0.005, 0.006, 0.006, 0.005, 0.006, 0.006, 0.005, 0.006, 0.007, 0.007, 0.007, 0.008, 0.007])

plt.scatter(x_vals, y_vals)
plt.grid(True)
plt.show()
