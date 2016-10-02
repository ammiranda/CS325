import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 5, 100)
y1 = np.exp(x)
y2 = np.power(2, x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.grid(True)
plt.savefig('../../img/question_4_plots/d.png')
