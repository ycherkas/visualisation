#За даними з таблиці побудувати 3d стовпчикову діаграму
import numpy as np
import matplotlib.pyplot as plt

german = (21.5, 54, 58, 64.1, 36.5, 87.5, 185, 385, 600, 710)
france = (22, 28.5, 40.5, 40, 31.5, 62.5, 130, 235, 330, 420)
gb = (38.5, 54.5, 73, 76, 66, 105, 160, 235, 320, 400)
belgium = (12.5, 15.5, 18.4, 16.8, 12.3, 27.5, 63, 112, 176, 214)

_x = np.arange(10)
_y = np.arange(4)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = belgium + gb + france + german
bottom = np.zeros_like(top)
width = depth = 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = np.array(top)
colors = plt.cm.jet(data.flatten()/float(data.max()))
bars = ax.bar3d(x, y, bottom, width, depth, top, shade=True, color = colors, alpha = 1)
ax.set_title('Export per year')
ax.set_xticklabels(('1900', '1913', '1929', '1938', '1950', '1960', '1970', '1980', '1990', '2000'))
ax.set_yticks(_y + width / 2)
ax.set_yticklabels(('Belgium', 'Great Britain', 'France', 'German'))
ax.set_xlabel('Year')
ax.set_zlabel('$, blns')

plt.show()