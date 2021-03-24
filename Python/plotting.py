# ---------------------------------------------------------------------------------------
#   Basic 2-D Line Plot
# ---------------------------------------------------------------------------------------
def plot_basic_2d(axhndl, x, y, tag='', descrip='', lnwidth=3, title='',
                  xlabel='', ylabel='', fontsize=16):

    # axhndl: axis handle
    # x: x data
    # y: y data
    # tag: label of data set - primarily used for creating a legend
    # descrip: color and line type
    # lnwidth: line width
    # title: plot title
    # xlabel: x axis label
    # ylabel: y axis label
    # fontsize: font size of xlabel, ylabel, and title

    axhndl.plot(x, y, descrip, label=tag, linewidth=lnwidth)
    axhndl.set_xlabel(xlabel, fontsize=fontsize)
    axhndl.set_ylabel(ylabel, fontsize=fontsize)
    axhndl.set_title(title, fontsize=fontsize)
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
#   Basic 3-D Contour Plot
# ---------------------------------------------------------------------------------------
def plot_contour(axhndl, x1, x2, func, fill=False, title='', xlabel='', ylabel='',
                 fontsize=16, colmap='bwr', cntrnum=15, lnlabels=False):

    # axhndl: axis handle
    # x1: independent variable #1
    # x2: independent variable #2
    # func: function handle of function to plot
    # fill: fill contour or just lines
    # title: plot title
    # xlabel: x axis label
    # ylabel: y axis label
    # fontsize: font size of xlabel, ylabel, and title
    # colmap: colormap to use for contour plot
    #   -> https://matplotlib.org/stable/tutorials/colors/colormaps.html
    # cntrnum: number of contours
    # lnlabels: whether or not to label contour lines

    import numpy as np  # necessary to run nxt ln
    xx1, xx2 = np.meshgrid(x1, x2)
    yy = func([xx1, xx2])
    if fill:
        cs = axhndl.contourf(xx1, xx2, yy, cntrnum, cmap=colmap)
        if lnlabels:
            axhndl.clabel(cs, inline=1, fontsize=8)
    else:
        cs = axhndl.contour(xx1, xx2, yy, cntrnum, cmap=colmap)
        if lnlabels:
            axhndl.clabel(cs, inline=1, fontsize=8)
    axhndl.set_xlabel(xlabel, fontsize=fontsize)
    axhndl.set_ylabel(ylabel, fontsize=fontsize)
    axhndl.set_title(title, fontsize=fontsize)
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
