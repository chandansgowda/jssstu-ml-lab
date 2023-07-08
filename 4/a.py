import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
labels = iris.feature_names

ax = plt.axes()
ax.boxplot(data)

ax.set_xticklabels(labels)
ax.set_ylabel('Value')
ax.set_title('Box Plot')

plt.show()