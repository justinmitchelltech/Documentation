import numpy as np
import matplotlib.pyplot as plt

from plotting import *
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
#    How to make a basic figure using plotting library
# ---------------------------------------------------------------------------------------

# 1. Plot Setup
plt.style.use('dark_background')
fig, ax = plt.subplots(2, 2, figsize=(12, 8), dpi=200)
'''
- Subplots:
     - If you just one one plot: plt.subplots(figsize=(12, 8), dpi=200)
     - If you have them stacked, ax is a 1-D array
     - If you have a grid of plots, ax is a 2-D array
- Plot Styles:
    https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
- Figure size (figsize) determines the size of the figure in inches.
- Dots per inches (dpi) determines how many pixels the figure comprises.
    - The default dpi in matplotlib is 100.
'''

# 2. Plotting
plot_basic_2d(ax[0, 0], np.linspace(-10, 10, 200), np.sin(np.linspace(-10, 10, 200)),
              title='Title or LaTeX: $\\pi^{xx}=2$', xlabel='x-axis', ylabel='y-axis',
              tag='first one')

plot_basic_2d(ax[1, 1], np.linspace(-10, 10, 200), np.cos(np.linspace(-10, 10, 200)),
              title='Title', xlabel='x-axis', ylabel='y-axis',
              descrip='g-.', tag='second one')


def func3d(x):
    return x[0]**2 + x[1]**2


plot_contour(ax[0, 1], np.linspace(-10, 10, 200), np.linspace(-10, 10, 200), func3d,
             lnlabels=False, fill=True)

# 3. Plot Labeling
ax[0, 0].legend()
ax[1, 1].legend()
fig.suptitle('all the plots', fontsize=40)

# 4. Show Plot
plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
