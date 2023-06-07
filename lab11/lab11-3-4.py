#3.	Визначити таке найменше значення розміру простору d, для якого виконується співвідношення (1)
#4.	Занулити λi, для яких d ≤ i ≤ n. Виконати зворотне перетворення та порівняти отримані данні з вихідними.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD

data = pd.read_csv('Wholesale customers data.csv').iloc[:,2:].values

svd = TruncatedSVD(n_components=data.shape[1]-1)
X_svd = svd.fit_transform(data)
own_values = svd.singular_values_

total = np.sum(own_values)
target_dimenstion_size = 0

for i in range(len(own_values)):
    current_sum = np.sum(own_values[:i+1])
    ratio = current_sum / total
    if ratio >= 0.8:
        break
    target_dimenstion_size = i

print('Target dimenstion size: ', i)

own_values[target_dimenstion_size-1:] = 0
svd.singular_values_ = own_values

data_inverse = svd.inverse_transform(X_svd)

np.set_printoptions(precision=1)
print('Original dataset:')
print(data[:3, :])
print('Restored dataset:')
print(data_inverse[:3, :])

plt.figure()
plt.plot(data)
plt.title('Original dataset')
plt.figure()
plt.plot(data_inverse)
plt.title('Restored dataset')
plt.show()