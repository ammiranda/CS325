import numpy as np
import matplotlib.pyplot as plt

x_vals = np.array([x for x in range(5, 31)])
y_vals = np.array([0.015, 0.015, 0.022, 0.048, 0.056, 0.083, 0.132, 0.209, 0.341, 0.533, 0.818, 1.189, 1.92, 3.087, 4.407, 6.66, 10.73, 17.35, 28.34, 45.86, 75.97, 122.9, 201.0, 322.8, 521.5, 850.0])

plt.scatter(x_vals, y_vals)
plt.grid(True)
plt.show()
