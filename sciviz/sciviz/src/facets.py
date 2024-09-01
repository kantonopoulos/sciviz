def axis_scales(scales):
    """Set the scales of the axes based on the input string.

    Args:
        scales (string): The scale type. One of 'fixed', 'free', 'free_x', or 'free_y'.

    Returns:
        bool: Whether the x-axis should be shared.
        bool: Whether the y-axis should be shared.
    """
    if scales == 'fixed':
        sharex = True
        sharey = True
    elif scales == 'free':
        sharex = False
        sharey = False
    elif scales == 'free_x':
        sharex = False
        sharey = True
    elif scales == 'free_y':
        sharex = True
        sharey = False
    return sharex, sharey


def calc_facet_legend_pos(ax):
    """Calculate the position of the legend on a FacetGrid.

    Args:
        ax (seaborn.axisgrid.FacetGrid): The FacetGrid to which the legend belongs.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The last axis of the FacetGrid.
        float: The x position of the legend.
        float: The y position of the legend.
    """
    last_ax = ax.axes.flat[-1]
    num_cols = ax._ncol
    
    for i, axis in enumerate(ax.axes.flat):
        if axis == last_ax:
            row, col = divmod(i, num_cols)
            row += 1
            col += 1

    pos_x = ax._ncol - col + 1.25 if ax._ncol != col else 1.25
    pos_y = 0.5 * ax._nrow + 0.2 if ax._nrow > 1 else 0.5
    
    return last_ax, pos_x, pos_y


def facets(ax, i, facettitles=None, facetlabel_size=11, facetlabel_weight='bold'):
    """Set the titles of the facets.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to set the facets on.
        i (int): The index of the facet.
        facettitles (list): The labels for the facets. Default is None.
        facetlabel_size (int): The font size of the facet labels. Default is 11.
        facetlabel_weight (str): The font weight of the facet labels. Default is 'bold'.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the theme set.
    """
    if facettitles is not None:
        ax.set_title(facettitles[i], weight=facetlabel_weight, fontsize=facetlabel_size)
    else:
        ax.set_title(format_string(ax.get_title()), weight=facetlabel_weight, fontsize=facetlabel_size)
    
    return ax