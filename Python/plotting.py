

def plot(handle, x, y, \
         descrip = '', \
         title = '', xlabel = '', ylabel = '', \
         fontsize = 16, label=''):

    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html


    '''
    Figure size (figsize) determines the size of the figure in inches.
    Dots per inches (dpi) determines how many pixels the figure comprises.
        - The default dpi in matplotlib is 100.
    '''

    handle.plot(x, y, descrip, label=label, linewidth=3)
    handle.set_xlabel(xlabel, fontsize=fontsize)
    handle.set_ylabel(ylabel, fontsize=fontsize)

    # plt.show()