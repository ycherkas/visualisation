#За даними з таблиці побудувати 2d стовпчикову діаграму
import numpy as np
import matplotlib.pyplot as plt

n_groups = 10
german = (21.5, 54, 58, 64.1, 36.5, 87.5, 185, 385, 600, 710)
france = (22, 28.5, 40.5, 40, 31.5, 62.5, 130, 235, 330, 420)
gb = (38.5, 54.5, 73, 76, 66, 105, 160, 235, 320, 400)
belgium = (12.5, 15.5, 18.4, 16.8, 12.3, 27.5, 63, 112, 176, 214)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.4
rects1 = ax.bar(index - bar_width, german, bar_width,
                alpha=opacity, color='b',
                label='Germany')
rects2 = ax.bar(index, france, bar_width,
                alpha=opacity, color='r',
                label='France')
rects3 = ax.bar(index + bar_width, gb, bar_width,
                alpha=opacity, color='g',
                label='Great Britain')
rects4 = ax.bar(index + 2*bar_width, belgium, bar_width,
                alpha=opacity, color='y',
                label='Belgium')
ax.set_xlabel('Year')
ax.set_ylabel('$, blns')
ax.set_title('Export per year')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('1900', '1913', '1929', '1938', '1950', '1960', '1970', '1980', '1990', '2000'))
ax.legend()

fig.tight_layout()
plt.grid(True)
plt.show()