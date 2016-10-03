import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import time

def fib_iter(n):
  cur_term = 0
  next_term = 1
  total = 0

  for k in range(0, n):
    total = cur_term + next_term
    next_term = cur_term
    cur_term = total
  
  return total

def generate_runtimes(k, n):
  times = []
  for i in range(k, n + 1):
    start_time = time.clock()
    fib_iter(i)
    times.append(1000 * (time.clock() - start_time))

  return times

y_vals_iter = generate_runtimes(5, 1000)

x_vals = np.array([x for x in range(5, 1001)])
y_vals = np.array(y_vals_iter)

lin_coefs = poly.polyfit(x_vals, y_vals, 1)
quad_coefs = poly.polyfit(x_vals, y_vals, 2)
cube_coefs = poly.polyfit(x_vals, y_vals, 3)

print(lin_coefs)

lin_fit = poly.polyval(x_vals, lin_coefs)
quad_fit = poly.polyval(x_vals, quad_coefs)
cube_fit = poly.polyval(x_vals, cube_coefs)

plt.plot(x_vals, lin_fit)
#plt.plot(x_vals, quad_fit)
#plt.plot(x_vals, cube_fit)
plt.plot(x_vals, y_vals, 'ko', markersize=2)
plt.grid(True)
plt.show()
