import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split

def manhattan_distance(x1, x2):
  distance = np.sum(np.abs(x1 - x2))
  return distance

class KNN:
  def __init__(self, k):
    self.k = k

  def fit(self, X, y):
    self.X_train = X
    self.y_train = y

  def predict(self, X):
    predictions = [self._predict(x) for x in X]
    return predictions

  def _predict(self, x):
    distances = [manhattan_distance(x, x_train) for x_train in self.X_train]
    k_indices = np.argsort(distances)[:self.k]
    k_nearest_labels = [self.y_train[i] for i in k_indices]
    most_common = Counter(k_nearest_labels).most_common()
    return most_common[0][0]

df = pd.read_csv('fruits.csv')
y = df['fruit_label'].values
X = df[['mass','width','height','color_score']].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

clf = KNN(k=5)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print("Predictions:",predictions)
accuracy = np.sum(predictions == y_test) / len(y_test)
print("Accuracy:", accuracy)