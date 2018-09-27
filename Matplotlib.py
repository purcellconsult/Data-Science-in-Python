"""simple plots with Matplotlib."""

import matplotlib.pyplot as plt

plt.axes()

circle = plt.Circle((0, 0), radius=0.50, fc='g')
plt.gca().add_patch(circle)

plt.axis('scaled')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size = 500)
plt.hist(x, normed=True, bins=50, color='green')
plt.ylabel('Probability')
plt.show()
