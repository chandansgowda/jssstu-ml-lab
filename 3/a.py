import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1,100,(30, 30))

plt.imshow(data, cmap="hot")
plt.colorbar()

plt.title("Heatmap")
plt.show()