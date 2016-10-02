import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

x_vals = np.array([x for x in range(5, 31)])
y_vals = np.array([0.005, 0.004, 0.003, 0.004, 0.004, 0.005, 0.005, 0.005, 0.005, 0.005, 0.006, 0.005, 0.005, 0.005, 0.006, 0.006, 0.005, 0.006, 0.006, 0.005, 0.006, 0.007, 0.007, 0.007, 0.008, 0.007])

lin_coefs = poly.polyfit(x_vals, y_vals, 1)
quad_coefs = poly.polyfit(x_vals, y_vals, 2)
cube_coefs = poly.polyfit(x_vals, y_vals, 3)

lin_fit = poly.polyval(x_vals, lin_coefs)
quad_fit = poly.polyval(x_vals, quad_coefs)
cube_fit = poly.polyval(x_vals, cube_coefs)

plt.plot(x_vals, lin_fit)
plt.plot(x_vals, quad_fit)
plt.plot(x_vals, cube_fit)
plt.scatter(x_vals, y_vals)
plt.grid(True)
plt.show()
