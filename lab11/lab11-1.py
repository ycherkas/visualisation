#1.	Використовуючи PCA візуалізувати данні у просторах з розмірностями два та три (2D та 3D)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

data = pd.read_csv('Wholesale customers data.csv')
X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

pca_2d = PCA(n_components=2)
pca_3d = PCA(n_components=3)
X_2d = pca_2d.fit_transform(X)
X_3d = pca_3d.fit_transform(X)

x_min, x_max = np.min(X_2d), np.max(X_2d)
X_2d = (X_2d - x_min) / (x_max - x_min)
x_min, x_max = np.min(X_3d), np.max(X_3d)
X_3d = (X_3d - x_min) / (x_max - x_min)

plt.figure()
plt.scatter(X_2d[:,0], X_2d[:,1], c = y)
plt.title('PCA 2D')
plt.figure()
plt.subplot(111, projection = '3d')
plt.scatter(X_3d[:,0], X_3d[:,1], X_3d[:,2], c = y)
plt.title('PCA 3D')
plt.show()