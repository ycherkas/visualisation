#2.	Використовуючи SVD, побудувати графік залежності власних значень матриці від їх номеру
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD

data = pd.read_csv('Wholesale customers data.csv')

svd = TruncatedSVD(n_components=data.shape[1])
svd.fit(data)

own_values = svd.singular_values_
idx_sorted = np.argsort(own_values)[::-1]
own_values_sorted = own_values[idx_sorted]

plt.plot(own_values_sorted, marker="*")
plt.xlabel('Index')
plt.ylabel('Own Value')
plt.grid(True)
plt.show()