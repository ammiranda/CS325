import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)
y1 = np.power(x, 0.75)
y2 = np.power(x, 0.5)

plt.plot(x, y1)
plt.plot(x, y2)

plt.grid(True)
plt.savefig('../../img/question_4_plots/a.png')
