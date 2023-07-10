import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("./ToyotaCorolla.csv")

sns.heatmap(data[["Price","KM","Doors", "Weight"]].corr(),cmap='jet')
plt.show()