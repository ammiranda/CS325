import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 100)
y1 = x * np.log2(x)
y2 = x * np.sqrt(x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.grid(True)
plt.savefig('../../img/question_4_plots/h.png')
