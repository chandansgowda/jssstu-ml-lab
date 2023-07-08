import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-1,1,100), np.ones(100))
y = x.copy().T
z = x**2 + y**2

ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z,cmap="jet")
ax.set_title("3D Surface Plot")

plt.show()