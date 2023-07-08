import matplotlib.pyplot as plt
import numpy as np

x = np.outer(np.linspace(-1,1,100), np.ones(100))
y = x.copy().T
z = x**2 + y**2

ax = plt.axes()
ax.contour(x, y, z, levels=20)
ax.set_title("Countour Plot")

plt.show()