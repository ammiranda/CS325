import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
from scipy.optimize import curve_fit

x_vals = np.array([x for x in range(5, 31)])
y_vals = np.array([0.015, 0.015, 0.022, 0.048, 0.056, 0.083, 0.132, 0.209, 0.341, 0.533, 0.818, 1.189, 1.92, 3.087, 4.407, 6.66, 10.73, 17.35, 28.34, 45.86, 75.97, 122.9, 201.0, 322.8, 521.5, 850.0])

def func(x, a, b, c):
  return a * np.exp(-b * x) + c

lin_coefs = poly.polyfit(x_vals, y_vals, 1)
quad_coefs = poly.polyfit(x_vals, y_vals, 2)
cube_coefs = poly.polyfit(x_vals, y_vals, 3)
four_coefs = poly.polyfit(x_vals, y_vals, 4)
popt, pcov = curve_fit(func, x_vals, y_vals, p0=(1, 1e-6, 1))
exp_yvals = func(x_vals, *popt)

lin_fit = poly.polyval(x_vals, lin_coefs)
quad_fit = poly.polyval(x_vals, quad_coefs)
cube_fit = poly.polyval(x_vals, cube_coefs)
four_coefs = poly.polyval(x_vals, four_coefs)

plt.plot(x_vals, lin_fit)
plt.plot(x_vals, quad_fit)
plt.plot(x_vals, cube_fit)
plt.plot(x_vals, four_coefs)
plt.plot(x_vals, exp_yvals)
plt.scatter(x_vals, y_vals)
plt.grid(True)
plt.show()
