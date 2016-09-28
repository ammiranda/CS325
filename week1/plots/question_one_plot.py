import math
import numpy as np
import matplotlib.pyplot as plt

xvals = np.arange(0.0, 50, 0.01)
y1 = 8 * np.log2(xvals)
y2 = xvals

plt.plot(xvals, y1)
plt.plot(xvals, y2)
plt.grid(True)
plt.show() 
