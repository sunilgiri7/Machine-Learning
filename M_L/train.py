from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from learn_KNN import KNN
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

iris = load_iris()
# df = pd.DataFrame(data = iris.data, columns=iris.feature_names)
# df['target'] = iris.target
# print(df.head())

X, y = iris.data, iris.target
# print(X)

# X = df.iloc[:, :4]
# y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

plt.figure()
plt.scatter(X[:,2], X[:,3], c=y, cmap=cmap, edgecolors='k', s=20)
# plt.show()

clf = KNN(k=5)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(y_pred) 

acc = np.sum(y_pred == y_test) / len(y_test)
print(acc)