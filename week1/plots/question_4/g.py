import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)
y1 = np.power(2, x)
y2 = scipy.misc.factorial(x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.grid(True)
plt.savefig('../../img/question_4_plots/g.png')
