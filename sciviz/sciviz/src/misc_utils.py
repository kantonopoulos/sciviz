def alpha_fill(ax, alpha):
    """
    Set the transparency of objects without chaninging their edge color.

    Args:
        ax (matplotlib.axes.Axes): The Axes object containing the bar plot.
        alpha (float): The transparency value for the bars.
    
    Returns:
        AxesSubplot: The matplotlib AxesSubplot object.

    """
    for patch in ax.patches:
            r, g, b, a = patch.get_facecolor()
            patch.set_facecolor((r, g, b, alpha))
    return ax


def edgecolor_pal(ax, fill, edgecolor, color_pal):
    """
    Sets the edgecolor of patches in the given ax object based on the color_pal.

    Args:
        ax (matplotlib.axes.Axes): The axes object to modify.
        fill (bool): Whether to fill the patches or not.
        edgecolor (str or None): The edgecolor to use for the patches. If None, the edgecolor will be set based on the color_pal.
        color_pal (list): A list of colors to use for setting the edgecolor of patches.

    Returns:
        matplotlib.axes.Axes: The modified axes object.

    """
    if fill != True and edgecolor == None:
        num_bars = len(ax.patches)
        for i in range(num_bars):
            ax.patches[i].set_edgecolor(color_pal[i])
    return ax


def count_values_ordered(data, color, order):
    """
    Counts the occurrences of each unique value in the specified column of a DataFrame and returns the counts in the specified order.

    Args:
        data (pandas.DataFrame): The DataFrame containing the data.
        color (str): The name of the column to count the values from.
        order (list or None): The desired order of the values. If None, the values will be returned in the default order.

    Returns:
        tuple: A tuple containing two lists. The first list contains the unique values in the specified order, and the second list contains the corresponding counts.

    """
    counts = data[color].value_counts()
    if order is not None:
        counts = counts.reindex(order)
    return counts.index.tolist(), counts.values.tolist()